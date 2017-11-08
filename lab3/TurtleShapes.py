import turtle
for i in range (5):
	turtle.left(145)
	turtle.forward(100)


# turtle.register_shape("hmmmm", ((50,50),(100,50),(50,0),(25,-25),(5)) )

turtle.register_shape("pentagon",((50,0),(50,50),(25,75),(0,50),(0,0)))
turtle.shape("pentagon")
turtle.right(95)
	

turtle.mainloop()



