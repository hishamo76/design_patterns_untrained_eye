from abc import ABC, abstractmethod
class AverageCalculator(ABC):

    def average(self):
        try:
            num_items = 0
            total_sum = 0
            while self.has_next():
                total_sum += self.next_item()
                num_items += 1
            if num_items == 0:
                raise RuntimeError("Can't compute the average of zero items.")
            return total_sum / num_items
        finally:
            self.dispose()

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next_item(self):
        pass

    def dispose(self):
        pass

class FileAverageCalculator(AverageCalculator):

    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ''

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result

    def dispose(self):
        self.file.close()


class MemoryAverageCalculator(AverageCalculator):
    def __init__(self, mem):
        self.mem = mem
    
    def has_next(self):
        return len(self.mem) > 0
    
    def next_item(self):
        if self.has_next():
            return self.mem.pop()

class GeneratorAdapter:
    def __init__(self,adaptee):
        self.adaptee=adaptee
    
    def readline(self):
        try:
            return next(self.adaptee)
        except StopIteration:
            return ''
    
    def close(self):
        pass


# mac = MemoryAverageCalculator([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
# print(mac.average())
from random import randint
g=(randint(1,100) for i in range(1000000))
fac=FileAverageCalculator(GeneratorAdapter(g))
print(fac.average())# Call the template method