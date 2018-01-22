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
			self.shape("circle")
			self.shapesize(radius/10)
			self.radius = radius
			self.color = color
	def move(self,height,width):
		currentx = self.xcor()
		newx = currentx + dx
		currenty = self.ycor()
		newy = currenty + dy
		right_side_ball = currentx + radius
		left_side_ball = currentx - radius
		upper_side_ball = currenty + radius
		lower_side_ball = currenty - radius
		if (upper_side_ball >= height or 
			lower_side_ball <= -height):
			newy = currenty - dy
		if (right_side_ball >= width or
			left_side_ball <= -width):
			newx = currentx - dx

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
	return (r,g,b)



def collide(ball1,ball2):
	if ball1 == ball2:
		return False
	distance = math.sqrt(math.pow(ball1.xcor()-ball2.xcor(),2)+math.pow(ball1.ycor()-ball2.ycor(),2))
	if distance +10 <= ball1.radius + ball2.radius :
		return True 
	else:
		return False 






 



