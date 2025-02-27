class Shape:
    width = 5
    height = 5
    printChar = '#'

    def printRow(self, i):
        raise NotImplementedError("Will be implemented in the child class")

    def print(self):
        for i in range(self.height):
            self.printRow(i)


class Square(Shape):
    def printRow(self, i):
        print(self.printChar * self.width)

class Triangle(Shape):
    def printRow(self, i):
        print(self.printChar * (i+1))


class SymmetricTriangle(Triangle):
    height = 5
    width = 2 * 5
    def printRow(self, i):
        triangleWidth = i * 2 + 1
        padding = int((self.width - triangleWidth)/2)
        print(' ' * padding + self.printChar * triangleWidth)

square = Square()
square.print()


triangle = Triangle()
triangle.print()


symmetricTriangle = SymmetricTriangle()
symmetricTriangle.print()