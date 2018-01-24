import turtle
import time 
import random
from starting import Ball 
from starting import random_color
from starting import collide 
import math 

turtle.colormode(255)
turtle.tracer(0)
turtle.hideturtle()

#def random_color():
#			r = random.randint(0,256) 
#			g = random.randint(0,256)
#			b = random.randint(0,256)
#			self.color((r,g,b))
#			return (r,g,b)


Running = True
sleep = 0.0077

SCREEN_WIDTH = turtle.getcanvas().winfo_width()/2
SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

MY_BALL = Ball(5,5,2,6,10,"pink") 

NUMBER_OF_BALLS = 6
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 100
MINIMUM_BALL_DX = -5
MAXIMUM_BALL_DX = 5
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 

BALLS = []
for i in range(NUMBER_OF_BALLS):
	x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
	y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
	dx = random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
	dy = random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
	while dx == 0:
		dx = random.randint(-250,250)
	while dy == 0:
		dy = random.randint(-250,250)
	radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
	color = (random.randint(0,255), random.randint(0,255) , random.randint(0,255))

	new_ball = Ball(x,y,dx,dy,radius, color)
	BALLS.append(new_ball)

def move_all_balls():
	for each_ball in BALLS:
		each_ball.move(SCREEN_HEIGHT,SCREEN_WIDTH)


def check_all_balls_collision():
	for ball1 in BALLS:
		for ball2 in BALLS:
			if collide(ball1,ball2) == True:
				x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx = random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				dy = random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				while dx == 0:
					dx = random.randint(-250,250)
				while dy == 0:
					dy = random.randint(-250,250)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = random_color()
				banana1 = ball1.radius
				banana2 = ball2.radius
				if banana1 > banana2:
					#ball1.radius = banana1 + 1
					#ball1.shapesize(ball1.radius/10)
					ball2.x = x
					ball2.y = y
					ball2.dx = dx
					ball2.dy = dy
					ball2.radius = radius 
					ball2.shade = color
					ball2.color(color)
					ball2.goto(x,y)	
					ball2.shapesize(ball2.radius/10)
				if banana1 < banana2:
					#ball2.radius = banana2 + 1
					#ball2.shapesize(ball2.radius/10)
					ball1.x = x 
					ball1.y = y
					ball1.dx = dx
					ball1.dy = dy
					ball1.radius = radius
					ball1.shade = color
					ball1.color(color)
					ball1.goto(x,y)
					ball1.shapesize(ball1.radius/10)


def check_myball_collision():
	for each_ball in BALLS:
		if collide(MY_BALL,each_ball)== True:
			my_radius = MY_BALL.radius
			enemy_radius = each_ball.radius 
			if MY_BALL.radius < each_ball.radius:
				return False
				#exit()
			else:
				x = random.randint(int(-SCREEN_WIDTH + MAXIMUM_BALL_RADIUS) , int(SCREEN_WIDTH - MAXIMUM_BALL_RADIUS))
				y = random.randint(int(-SCREEN_HEIGHT + MAXIMUM_BALL_RADIUS) , int(SCREEN_HEIGHT - MAXIMUM_BALL_RADIUS))
				dx = random.randint(int(MINIMUM_BALL_DX),int(MAXIMUM_BALL_DX))
				dy = random.randint(int(MINIMUM_BALL_DY),int(MAXIMUM_BALL_DY))
				while dx == 0:
					dx = random.randint(MINIMUM_BALL_DX,MAXIMUM_BALL_DX)
				while dy == 0:
					dy = random.randint(MINIMUM_BALL_DY,MAXIMUM_BALL_DY)
				radius = random.randint(MINIMUM_BALL_RADIUS,MAXIMUM_BALL_RADIUS)
				color = random_color()
				MY_BALL.radius = my_radius + 1
				MY_BALL.shapesize(MY_BALL.radius/10)
				each_ball = Ball(x,y,dx,dy,radius,color)
				return True


def movearound(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while Running == True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH =  turtle.getcanvas().winfo_width()/2

	if SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	move_all_balls()
	MY_BALL.move(SCREEN_WIDTH,SCREEN_HEIGHT)
	if check_myball_collision() == False:
		Running = False
	else:
		Running = True
	turtle.getscreen().update()
	time.sleep(0.077)

	check_all_balls_collision()
	turtle.getscreen().update()
	