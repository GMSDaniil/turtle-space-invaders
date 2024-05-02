from turtle import Turtle
from random import choice, random, randint

class Layout():
    def __init__(self) -> None:
        self.stars = []
        self.star_speed = 1
        self.chance = 0.03
        self.create_star()
    
    def create_star(self):
        if random() < self.chance:
            t = Turtle(shape="square")
            t.color(choice(["white", "grey"]))
            t.shapesize(0.1, 0.1 , 1)
            self.stars.append(t)
            y = 300
            x = randint(-240,240)
            self.stars[-1].up()
            self.stars[-1].goto(x,y)

    def move_stars(self):
        for i in self.stars:
            i.goto(i.xcor()+randint(-1,1), i.ycor()-self.star_speed)
        # while self.stars and self.stars[0].ycor() > 300:
        #     self.stars.pop(0)

