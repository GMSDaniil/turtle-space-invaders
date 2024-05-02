import turtle
import random
turtle.register_shape('red.gif')
turtle.register_shape('yellow.gif')
turtle.register_shape('green.gif')
shape = ((0,0), (3,0), (0,3), (3,3))
turtle.register_shape('patron', shape)

class Enemy_Patron():
    def __init__(self) -> None:
        self.patrons = []
        
    def create_patron(self,x,y):
        patron = turtle.Turtle(shape='patron')
        patron.up()
        patron.color('green')
        patron.goto(x=x, y=y-20)
        self.patrons.append(patron)

    def move(self):
        for i in self.patrons:
            i.goto(x=i.xcor(), y=i.ycor()-4)

    def hide(self, patron):
        patron.hideturtle()
        del patron




class Aliens():
    def __init__(self) -> None:
        self.patrons = Enemy_Patron()
        self.green = []
        self.yellow = []
        self.red = []
        self.arrays = [self.green, self.yellow, self.red]
        self.shoot_chance = 0.04
        self.direction = 1
        self.speed = 0.7
        self.create_aliens()


    def shoot(self):
        # if random.random() < self.shoot_chance:
        for col in range(10):
            if self.red[col] != 'shot':
                if random.random() < self.shoot_chance:
                    self.patrons.create_patron(self.red[col].xcor(), self.red[col].ycor())
                continue
            elif self.yellow[col] != 'shot':
                if random.random() < self.shoot_chance:
                    self.patrons.create_patron(self.yellow[col].xcor(), self.yellow[col].ycor())
                continue
            elif self.green[col] != 'shot':
                if random.random() < self.shoot_chance:
                    self.patrons.create_patron(self.green[col].xcor(), self.green[col].ycor())
                continue

    def create_aliens(self):
        shapes = ['green.gif', 'yellow.gif', 'red.gif']
        
        for j in range(3):
            for i in range(10):
                x = turtle.Turtle(shape=shapes[j])
                x.up()
                x.goto(x=-200+30*i, y = 250-25*j)
                x.shapesize(0.5, 0.5, 1)
                self.arrays[j].append(x)

    def change_direction(self):
        self.direction *= -1
        for typ in self.arrays:
            for alien in typ:
                if alien == 'shot':
                    continue
                alien.goto(alien.xcor()+self.direction*self.speed, alien.ycor()-20)

    def move(self):
        for typ in self.arrays:
            x = 0
            y = 9
            while x < 9 and typ[x] == 'shot':
                x += 1
            while  y > 0 and typ[y] == 'shot':
                y -= 1

            if (typ[y] != 'shot' and typ[y].xcor() > 230) or (typ[x] != 'shot' and typ[x].xcor() < -235):
                self.change_direction()
                return

        for typ in self.arrays:
            for alien in typ:
                if alien == 'shot':
                    continue
                alien.goto(alien.xcor()+self.direction*self.speed, alien.ycor())

    def patron_shot(self, patron):
        for typ in self.arrays:
            for i, alien in enumerate(typ):
                if alien == 'shot':
                    continue
                if patron.distance(alien) < 10:
                    alien.hideturtle()
                    typ[i] = 'shot'
                    self.speed += 0.03
                    self.shoot_chance += 0.003
                    return True
        return False
    
    def reached_ship(self):
        for typ in self.arrays:
            for alien in typ:
                if alien == 'shot':
                    continue
                if alien.ycor() <= -220:
                    return True
                    