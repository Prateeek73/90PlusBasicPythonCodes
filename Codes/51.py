class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def area(self):
        return self.length*self.width
aSquare= Rectangle(3,5)
print(aSquare.area())