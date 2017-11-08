# import turtle
# turtle.speed(100)
# turtle.addshape("cookie.gif")
# turtle.shape("cookie.gif")
# for i in range (200):
# 	turtle.forward(100)
# 	turtle.right (64)
# 	turtle.forward(250)
# 	turtle.right(64)
# 	turtle.forward(100)
# 	turtle.home()
# 	turtle.right(10)





# turtle.mainloop()

import turtle
turtle.tracer(0,1)
for i in range(360):
	turtle.right(i)
	turtle.forward(200)
	turtle.right(60)
	turtle.forward(50)
	turtle.right(60)
	turtle.forward(30)
	turtle.pu()
	turtle.home()
	turtle.pd()



turtle.mainloop()