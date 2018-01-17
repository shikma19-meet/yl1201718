from  turtle import *
import random 



def Ball(Turtle):
	def __init__ (self,x,y,dx,dy,radius,color):
			Turtle.__init__(self)
			self.pu()
			self.goto(x,y)
			self.dx = dx
			self.dy = dy
			self.shape("circle")
			self.shapesize(radius/10)
			self.radius = radius
			self.color = color
			self.color(color)
	def move(self):
		currentx = self.xcor()
		newx = currentx + dx
		currenty = self.ycor()
		newy = currenty + dy
		right_side_ball = currentx + radius
		left_side_ball = currentx - radius
		upper_side_ball = currenty + radius
		lower_side_ball = currenty - radius
		self.goto(newx, newy)

	

		if right_side_ball > 300:
			newx = currenty - dx

		elif left_side_ball < -300:
			newx = currentx + dx

		elif upper_side_ball > 300:
			newy = currenty - dy

		elif lower_side_ball < -300:
			newy = currenty + dy 

def random_color():
	r = random.randint(0,256) 
	g = random.randint(0,256)
	b = random.randint(0,256)
	self.color((r,g,b))
	return (r,g,b)
