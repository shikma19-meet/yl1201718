from turtle import * 
import time 
import random
from starting import Ball 
from starting import random_color
from starting import collide 
import math 

colormode(255)
tracer(0)
hideturtle()

#def random_color():
#			r = random.randint(0,256) 
#			g = random.randint(0,256)
#			b = random.randint(0,256)
#			self.color((r,g,b))
#			return (r,g,b)


Running = True
sleep = 0.0077

SCREEN_WIDTH = getcanvas().winfo_width()/2
SCREEN_HEIGHT = getcanvas().winfo_height()/2

MY_BALL = (5,5,2,6,3,"pink") 

NUMBER_OF_BALLS = 50
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
	color = random_color()

	new_ball = Ball(x,y,dx,dy,radius,color)
	BALLS.append(new_ball)

def move_all_balls():
	for each_ball in BALLS:
		each_ball.move(SCREEN_HEIGHT,SCREEN_WIDTH)


def check_all_balls_collision():
	for ball1 in BALLS:
		for ball2 in BALLS:
			if collide(ball1,ball2) == True:
				print(f"{ball1} and {ball2} collided")
			else:
				print(f"{ball1} and {ball2} did NOT collide")


check_all_balls_collision()



# this is were I stopped: 2. Create a nested for-loop in which both loops iterate through BALLS. Use ball_a as the variable name for the first loop and ball_b for the second loop
# I wrote the loop, but need to change what happens when they collide. 


