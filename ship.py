import turtle
turtle.register_shape('spaceship.gif')
turtle.register_shape('heart.gif')
shape = ((0,0), (3,0), (0,3), (3,3))
turtle.register_shape('patron', shape)

class Patron():
    def __init__(self) -> None:
        self.patrons = []
        
    def create_patron(self,x,y):
        patron = turtle.Turtle(shape='patron')
        patron.up()
        patron.color('white')
        patron.goto(x=x-2, y=y+20)
        self.patrons.append(patron)

    def move(self):
        for i in self.patrons:
            i.goto(x=i.xcor(), y=i.ycor()+3.5)

    def hide(self, patron):
        patron.hideturtle()
        del patron
        
        



class Spaceship(turtle.Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape('spaceship.gif')
        self.shapesize(0.2, 0.2, 1)
        self.up()
        self.goto(x=0, y=-230)
        self.health = []
        self.add_health()

    def add_health(self):
        for i in range(3):
            x = turtle.Turtle(shape='heart.gif')
            x.up()
            x.goto(x=-30+i*25, y=-280)
            self.health.append(x)


    def move_left(self):
        if self.xcor()-1.5 < -230:
            self.goto(-230, self.ycor())
            return
        self.goto(self.xcor()-1.5, self.ycor())

    def move_right(self):
        if self.xcor()+1.5 > 225:
            self.goto(225, self.ycor())
            return
        self.goto(self.xcor()+1.5, self.ycor())
    
    