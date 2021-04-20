from turtle import Turtle

class Car(Turtle):

    def __init__(self, x_coordinate, y_coordinate, color):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.penup()
        self.setposition(x_coordinate, y_coordinate)
        self.setheading(180)
        self.turtlesize(1, 2)

    def move(self, distance):
        self.forward(distance)
