#BACKGROUND AND TITLE OF GAME

import turtle
#this import turtle which is common used by games is build in unlike pygame
import os

wn = turtle.Screen()
#windows
#S capitalize is important!
#this is the title of the game
wn.title(Pong Game)
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
#this stops the window from updating. Speeds up game the 0 say's is set to

#SCORE
#turlte name of class Turtle name of the turtle
score_a = 0
score_b = 0

#PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
#animation speed is set to max
paddle_a.shape("square")
#does it connect to turtle?
paddle_a.color("white")
#color of the paddle
paddle_a.shapesize(strech_wid=5, strech_len=1)
#5 *20 = 100 makes it that size
paddle_a.penup()
#a function for turtle
paddle_a.goto(-350, 0)
#first one is an x-coordinate the 0 for in the middle


#PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
#animation speed is set to max
paddle_b.shape("square")
#does it connect to turtle?
paddle_b.color("white")
#color of the paddle
paddle_b.shapesize(strech_wid=5, strech_len=1)
#5 *20 = 100 makes it that size
paddle_b.penup()
#a function for turtle
paddle_b.goto(350, 0)
#first one is an x-coordinate makes it go right on the screen the 0 for in the middle

#BALL 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
#2 means ball moves by 2px x is negatieve so it moves right y is postive so it moves to the left

#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
oen.hideturtle()
pen.goto(260, 0)
pen.write("Player A: 0  Player B: 0" align="center", font=("Courier", 24, "normal"))


#FUNCTION
def paddle_a_up():
  y = paddle_a.ycor()
#paddle is name of the object
#ycor is from the turtle/increases as it go up decreased when it goes down
  y += 20
  paddle_a.sety(y)

def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)


def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y)

def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)

#KEYBOARD BINDING
#here is where we call the function we have define it but, it needs to be called
wn.listen()
#tells it is a keyboard event listener
wn.onkeypress(padd_a_up, "w")
#when the usser presses lowercase w the function will call paddle a-up
wn.onkeypress(padd_a_down, "s")
wn.onkeypress(padd_b_down, "UP")
wn.onkeypress(padd_b_down, "DOWN")

#MAIN GAME LOOP

while True:
#remeber the 4 spaces
  wn.update()
#every time loops runs it update the screen
  
  #MOVE THE BALL
  ball.setx(ball.xcor() + ball.dx)
  #it combines what u did above/ball starts at 0 0
  ball.sety(ball,ycor() + ball.dy)

  #BORDER CHECKING
  if ball.ycor() > 290:
    ball.sety(290)
    #because of the screenwidth 600
    ball.dy *= -1
    #revers ball in negative direction
    os.system("afplay bounch.wav&")

  if ball.ycor() > -290:
    ball.sety(-290)
    #because of the screenwidth 600
    ball.dy *= -1
    #revers ball in negative direction
    os.system("afplay bounch.wav&")


  if ball.xcor() > 390:
  #width was 800 so that makes 400
  bal.goto(0, 0)
  ball.dx *= -1
#oposite direction
  score_a += 1
  pen.clear()
  pen.write("Player A: {}  Player B: {}".format(score_a, score_b) align="center", font=("Courier", 24, "normal"))


if ball.xcor() > -390:
  #width was 800 so that makes 400
  bal.goto(0, 0)
  ball.dx *= -1
  score_b += 1
  pen.clear()
  pen.write("Player A: {}  Player B: {}".format(score_a, score_b) align="center", font=("Courier", 24, "normal"))

  #PADDLE AND BALL COLLISOIONS
  if ball.xcor() > 340 and ball.xcor() < 350 (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle.b.cor() -40):
    ball.setx(340)
    ball.dx *= -1
    #this has to do with the paddle so it hits the center of it
    os.system("afplay bounch.wav&")

    
    if ball.xcor() > -340 and ball.xcor() > -350 (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle.b.cor() -40):
    ball.setx(340)
    ball.dx *= -1
    #this has to do with the paddle so it hits the center of it
    os.system("afplay bounch.wav&")
