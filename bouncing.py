import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Simulator")
wn.tracer(0)


ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")

ball.speed(0)
ball.goto(0,200)
ball.dy = 0
ball.dx = 20


g = -2

while True:
    wn.update()
    ball.dy += g
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)

    if ball.ycor() < -300:
        ball.dy *= -1
    
    if ball.xcor() < -300 or ball.xcor() > 300:
        ball.dx *= -1

    

    