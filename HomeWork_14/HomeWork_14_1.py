class Shape:

    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self, width):
        self.width = width

    def draw(self):
        for i in range(1, self.width + 1):
            for j in range(i):
                print("*", end="")
            print()


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def draw(self):
        for i in range(self.width):
            for i in range(self.heigth):
                print("*", end="")
            print()


t = Triangle(7)
r = Rectangle(7, 7)
l = []
l.append(t)
l.append(r)
for i in l:
    i.draw()
    print()
