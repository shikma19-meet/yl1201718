from turtle import *
import random 
import math

class Ball (Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
#def random_color():
#			r = random.randint(0,256) 
#     		b = random.randint(0,256)
#			self.color((r,g,b))
			 

Ball1 = Ball(2,"pink",9999)
Ball2 = Ball(7,"black",1)

Ball1.goto(100,100)

def check_collision(ball1,ball2):
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.xcor()
	y2 = ball2.xcor()
	d= math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
	if d  > 0:
		print("the balls  don't coolide")
		if Ball1.radius > Ball2.radius:
			Ball2.goto(Ball2.xcor()+15,Ball2.ycor()+15)
		else:
			Ball1.goto(Ball1.xcor()+15,Ball2.ycor()+15)

	elif  d== 0:
		print("the balls coolide")
		if Ball1.radius > Ball2.radius:
			Ball2.goto(Ball2.xcor()+15,Ball2.ycor()+15)
		else:
			Ball1.goto(Ball1.xcor()+15,Ball2.ycor()+15)
		#ball1.random_color() 
	else :#ball2.random_color()
		print("the balls coolide")
check_collision(Ball1,Ball2)	
if Ball1.radius + Ball1.xcor() >= 300:
	print("the ball went off the edge 1")
elif Ball1.radius - Ball1.xcor() >= -300 :
	print("the ball went off the edge 2")
elif Ball1.radius + Ball1.ycor() >= 250 :
	print("the ball went off the edge 3")
elif Ball1.radius - Ball1.ycor() <= -250:
	print("the ball went off the edge 4")
else :
	print("everything is fine ")




#if the xcor of the ball + rad is bigger than the width
#


mainloop()
