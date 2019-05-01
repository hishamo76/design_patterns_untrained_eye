class Duck:

    def quack(self):
      print('Quack')

    def fly(self):
        print("I'm flying")


class Turkey:

    def gobble(self):
        print('Gobble gobble')

    def fly(self):
        print("I'm flying a short distance")

class TurkeyAdapter:

    def __init__(self, adaptee):
        self.turkey = adaptee
    def quack(self):
        pass
    def fly(self):
        for i in range(5):
            self.adaptee.fly()
