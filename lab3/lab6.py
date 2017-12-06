from turtle import *
import random 
import math
def random_color():
			r = random.randint(0,256) 
			g = random.randint(0,256)
			b = random.randint(0,256)
			self.color((r,g,b))

class Ball (Turtle):
	def __init__(self,radius,color,speed):
		Turtle.__init__(self)
		self.shape("circle")
		self.shapesize(radius/10)
		self.radius = radius
		self.color(color)
		self.speed(speed)
			 

Ball1 = Ball(10,"pink",5000)
Ball2 = Ball(70,"black",3)

def check_collision(ball1,ball2):
	x1 = ball1.xcor()
	x2 = ball2.xcor()
	y1 = ball1.xcor()
	y2 = ball2.xcor()
	d= math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2))
	if d  > 0:
		print("the balls  don't coolide")
	elif  d== 0:
		random_color() 
	else :
		random_color()
check_collision(Ball1,Ball2)	
mainloop()
