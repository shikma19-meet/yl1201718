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

MY_BALL = Ball(5,5,0,0,25,"pink") 


NUMBER_OF_BALLS = 4
MINIMUM_BALL_RADIUS = 10
MAXIMUM_BALL_RADIUS = 30
MINIMUM_BALL_DX = -10
MAXIMUM_BALL_DX = 10
MINIMUM_BALL_DY = -5
MAXIMUM_BALL_DY = 5 
last_haert = time.time()
amount_of_lives = 5
score = 0
writescore = turtle.clone()
writescore.color("orange")
writescore.ht()
before_writescore = turtle.clone()
before_writescore.color("orange")
before_writescore.ht()


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
				each_ball.goto(each_ball.x + 50 , each_ball.y + 50)
				return False
				#exit()
			else:
				global score 
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
				each_ball.x = x 
				each_ball.y = y
				each_ball.dx = dx
				each_ball.dy = dy
				each_ball.radius = radius
				each_ball.shade = color
				each_ball.color(color)
				each_ball.goto(x,y)
				each_ball.shapesize(each_ball.radius/10)
				score = score + 1
				writescore.goto(SCREEN_WIDTH-100,SCREEN_HEIGHT-75)
				writescore.clear()
				writescore.write(score, font=("Arial", 16, "normal"))
				before_writescore.goto(SCREEN_WIDTH-170,SCREEN_HEIGHT-75)
				before_writescore.clear()
				before_writescore.write("score:", font=("Arial", 16, "normal"))


				

def movearound(event):
	MY_BALL.goto(event.x - SCREEN_WIDTH,SCREEN_HEIGHT - event.y)

turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while Running == True:
	if SCREEN_WIDTH != turtle.getcanvas().winfo_width()/2:
		SCREEN_WIDTH =  turtle.getcanvas().winfo_width()/2

	if SCREEN_HEIGHT != turtle.getcanvas().winfo_height()/2:
		SCREEN_HEIGHT = turtle.getcanvas().winfo_height()/2

	if MY_BALL.radius > MAXIMUM_BALL_RADIUS:
		turtle.goto(SCREEN_WIDTH/2-75,SCREEN_HEIGHT/2)
		turtle.color("blue")
		turtle.write("you won,good job!", font=("Arial", 16, "normal"))
		print(MY_BALL.radius)
		time.sleep(3)
		quit()



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
	
	if Running == False:
		print(amount_of_lives)
		amount_of_lives = amount_of_lives -1 
		Running = True
	if amount_of_lives <= 0:
		turtle.color("orange")
		turtle.goto(SCREEN_WIDTH - 300 , SCREEN_HEIGHT - 75)
		turtle.write("you're out of lives, you die!", font=("Arial", 16, "normal"))
		time.sleep(3)
		quit()

	starting_time = time.time()
	if last_haert + 30 < time.time():
		amount_of_lives = amount_of_lives + 1
		last_haert = time.time()
		print(amount_of_lives)
	turtle.pu()
	turtle.goto(SCREEN_WIDTH-380,SCREEN_HEIGHT-75)
	turtle.clear()
	turtle.color("orange")
	turtle.write("Lives:", font=("Arial", 16, "normal"))
	turtle.goto(SCREEN_WIDTH-300,SCREEN_HEIGHT-75)
	turtle.write(amount_of_lives, font=("Arial", 16, "normal"))



