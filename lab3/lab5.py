from turtle import *
import random
colormode(255)
class Square(Turtle):
	def __init__ (self, size):
		Turtle.__init__(self)
		self.shape ("square")
		self.shapesize()
	def random_color(self):
		r = random.randint(0,256) 
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color((r,g,b))


class Hexagon(Turtle):
	def __init__(self,size):
		Turtle.__init__(self)
		self.begin_poly()
		for i in range (6):
			self.forward(10)
			self.right(60)
		self.end_poly()
		x= self.get_poly()
		register_shape("x", x)
		self.shape("x")
	def random_color(self):
		r = random.randint(0,256) 
		g = random.randint(0,256)
		b = random.randint(0,256)
		self.color((r,g,b))

class Rectangle(Turtle):
	def __init__(self,width,hight):
		Turtle.__init__(self)
		register_shape("Rectangle",((0,hight),(width,hight),(width,0),(0,0)))
		self.shape("Rectangle")
	def random_color(self):
			r = random.randint(0,256) 
			g = random.randint(0,256)
			b = random.randint(0,256)
			self.color((r,g,b))

class Square2(Rectangle):
	def __init__(self,size):
		Rectangle.__init__(self,size,size)
	def random_color(self):
			r = random.randint(0,256) 
			g = random.randint(0,256)
			b = random.randint(0,256)
			self.color((r,g,b))
r = random.randint(0,256) 
g = random.randint(0,256)
b = random.randint(0,256)
class polygon(Turtle):
	def __init__(self,lines,size):
		Turtle.__init__(self)
		angle = 360/lines 
		self.color((r,g,b))
		self.begin_fill()
		for i in range(lines):
			self.forward(size)
			self.right(angle)
		self.end_fill()


	

# square1 = Square(10)
# square1.random_color()
# Hexagon1 = Hexagon(20)
# Hexagon1.random_color()
# Rectangle1  = Rectangle(20,40)
# Rectangle1.random_color()
#New_square = Square2(20)
#New_square.random_color()
Polygon1 = polygon(4,100)







mainloop()

