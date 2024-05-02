from turtle import Screen, Turtle
from layout import Layout
from ship import Spaceship
from ship import Patron
from enemies import Aliens
import time
import random
import keyboard

screen = Screen()
screen.setup(width=500, height=600)
screen.bgcolor("#1b1e1f")
screen.title("Space Invaders")
screen.tracer(0)

enemies = Aliens()
layout = Layout()
ship = Spaceship()
patrons = Patron()


class Game():
    def __init__(self) -> None:
        self.shooting_time = time.time()
        self.x = Turtle()
        self.x.hideturtle()
        self.x.up()
        self.x.goto(0,0)
        self.x.color("white")
        self.x.write("Shooting: \"↑\"\nMoving: \"←\" and \"→\"\nPress Enter to continue.", move=False, align="center", font=("Courier", "15", "normal"))
        self.game_is_on= True

    def start(self):
        self.x.clear()
        

        def shoot():
            if time.time() - self.shooting_time > 0.5:
                self.shooting_time = time.time()
                patrons.create_patron(x=ship.xcor(), y=ship.ycor())


        while self.game_is_on:
            time.sleep(0.01)
            screen.update()
            layout.create_star()
            layout.move_stars()
            patrons.move()
            enemies.move()
            enemies.patrons.move()
            if random.random() < 0.1:
                enemies.shoot()
            for i, patron in enumerate(patrons.patrons):
                if enemies.patron_shot(patron):
                    patron.hideturtle()
                    patrons.patrons.pop(i)

            for i, patron in enumerate(enemies.patrons.patrons):
                if ship.distance(patron) < 13:
                    patron.hideturtle()
                    enemies.patrons.patrons.pop(i)

                    if len(ship.health) > 1:
                        ship.health[-1].hideturtle()
                        ship.health.pop()
                        ship.hideturtle()
                        
                        time.sleep(2)
                        while len(enemies.patrons.patrons) > 0:
                            enemies.patrons.patrons[-1].hideturtle()
                            enemies.patrons.patrons.pop()
                        ship.goto(0, -230)
                        ship.showturtle()

                    else:
                        
                        self.game_over()
            

            if enemies.reached_ship():
                self.game_over()

            if set(enemies.green) == set(enemies.yellow) == set(enemies.red):
                self.you_won()



                    

            if keyboard.is_pressed("Left"):
                ship.move_left()
            elif keyboard.is_pressed("Right"):
                ship.move_right()

            screen.onkey(shoot,"Up")
    

    def game_over(self):
        self.game_is_on = False
        ship.hideturtle()
        x = Turtle()
        x.hideturtle()
        x.up()
        x.goto(0,0)
        x.color("white")
        x.write("Game Over!", move=False, align="center", font=("Courier", "20", "bold"))

    def you_won(self):
        self.game_is_on = False
        for i in range(100):
            time.sleep(0.01)
            while len(enemies.patrons.patrons) > 0:
                enemies.patrons.patrons[-1].hideturtle()
                enemies.patrons.patrons.pop()
            screen.update()
            patrons.move()
            layout.create_star()
            layout.move_stars()
            ship.goto(ship.xcor(), ship.ycor()+7)
        x = Turtle()
        x.hideturtle()
        x.up()
        x.goto(0,0)
        x.color("white")
        x.write("You Won!", move=False, align="center", font=("Courier", "20", "bold"))






        


screen.listen()
game = Game()

screen.onkey(game.start, "Return")
# screen.onkey(game.start, "Right")

screen.update()
screen.mainloop()