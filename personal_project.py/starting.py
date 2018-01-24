from  turtle import *
import random 
import math


class Ball(Turtle):
	def __init__ (self,x,y,dx,dy,radius,color):
			Turtle.__init__(self)
			self.pu()
			self.goto(x,y)
			self.dx = dx
			self.dy = dy
			self.x = x
			self.y = y
			self.shape("circle")
			self.shapesize(radius/10)
			self.radius = radius
			self.shade = color
			self.color(color)
	def move(self,height,width):
		currentx = self.xcor()
		newx = currentx + self.dx
		currenty = self.ycor()
		newy = currenty + self.dy
		right_side_ball = newx + self.radius
		left_side_ball = newx - self.radius
		upper_side_ball = newy + self.radius
		lower_side_ball = newy - self.radius
		self.goto(newx, newy)
		if (upper_side_ball >= height or 
			lower_side_ball <= -height):
			self.dy = -self.dy
		if (right_side_ball >= width or
			left_side_ball <= -width):
			self.dx = -self.dx

		
def random_color():
	r = random.randint(0,255) 
	g = random.randint(0,255)
	b = random.randint(0,255)
	return (r,g,b)



def collide(ball1,ball2):
	if ball1 == ball2:
		return False
	distance = math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))
	if distance +10 <= ball1.radius + ball2.radius:
		return True 
	else:
		return False