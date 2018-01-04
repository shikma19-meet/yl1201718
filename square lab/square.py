from turtle import * 
class Rectangle(Turtle):
	def __init__(self,width,height):
		Turtle.__init__(self)
		register_shape("Rectangle",((0,height),(width,height),(width,0),(0,0)))
		self.shape("Rectangle")
		self.height = height
		self.width = width
	def top(self):
		return self.ycor()+self.height
	def bottom(self):
		return self.ycor()
	def right(self):
		return self.xcor()+self.width
	def left(self):
		return self.xcor()



rectangle1= Rectangle(10,50)
rectangle1.penup()
rectangle1.goto(100,40)
fred = Rectangle(40,70)

def check_collision(r1,r2):
	#print(r1.height())
	if (r1.top() >= r2.bottom() and 
		r1.right() >= r2.left() and 
		r1.bottom() <= r2.top() and 
		r1.left() <= r2.right()):
		print("the rectangles collide")
	else :
		print("the rectangles don't coolide")


check_collision(rectangle1,fred)
mainloop()