import turtle

class pattern():
    def __init__(self, angle, times):
        self.__angle = angle # Integer
        self.__times = times # Integer

    def draw_pattern(self):
        colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
        turtle.setup(800, 600)  # setting window dimensions
        turtle.bgcolor('black')
        for x in range(self.__times):
            turtle.pencolor(colors[x % 6])
            turtle.width(x / 100 + 1)
            turtle.forward(x)
            turtle.left(self.__angle)
        turtle.done()

mypattern = []

try:
    with open("patterns.txt") as f:
        for i in range(0, 10, 2):
            angle = f.readline().strip()
            times = f.readline().strip()
            mypattern.append(pattern(int(angle), int(times)))
except FileNotFoundError:
    print("File not found.")

mypattern[0].draw_pattern()
mypattern[1].draw_pattern()
mypattern[2].draw_pattern()
mypattern[3].draw_pattern()
mypattern[4].draw_pattern()
