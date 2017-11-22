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

square1 = Square(10)
square1.random_color()
Hexagon1 = Hexagon(20)
mainloop()

