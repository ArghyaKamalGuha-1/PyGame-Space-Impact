
#argya.spaceimpact@
#Space Impact
#Image for Impact
#Image for Player
#Image for background

#Python on windows
import turtle
import os
import math
import random
import winsound
import sys

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Space Impact")
wn.bgpic("space_impact_background.gif")

#Register the shapes
turtle.register_shape("invader2.gif")
turtle.register_shape("player.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("end.gif")
#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("orange")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(10)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

#Set the score to 0
score = 0

#Draw the score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("orange")
score_pen.penup()
score_pen.setposition(-280, 260)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Bold", 22, "bold"))
score_pen.hideturtle()

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Choose a number of enemies
number_of_enemies = 4
#Create an empty list of enemies
enemies = []

#Add enemies to the list
for i in range(number_of_enemies):
#Create the enemy
	enemies.append(turtle.Turtle())

for enemy in enemies:	
 
       
	enemy.color("orange")
	enemy.shape("invader2.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)
	enemy.setheading(270)

enemyspeed = 2


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("invader.gif")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.8, 0.8)
bullet.hideturtle()

bulletspeed = 38


#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
		#sound while the moves
	winsound.PlaySound("beep.wav" ,winsound.SND_ASYNC)
	player.setx(x)
	
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	winsound.PlaySound("beep.wav" ,winsound.SND_ASYNC)	
	player.setx(x)
def move_down():
        
        y = player.ycor()
        y -= playerspeed
        if y < -280:
                y = - 280
        winsound.PlaySound("beep.wav" ,winsound.SND_ASYNC)        
        player.sety(y)

def move_up():
        y = player.ycor()
        y += playerspeed
        if y > 280:
                y = 280
        winsound.PlaySound("beep.wav" ,winsound.SND_ASYNC)        
        player.sety(y)
	
def fire_bullet():
	#Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
                #Move the bullet to the just above the player
		winsound.PlaySound("laser3.wav" ,winsound.SND_ASYNC)
		#Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 5
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
               
		return True
	else:
		return False
                            	
#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_down, "Down")
turtle.onkey(move_up, "Up")
turtle.onkey(fire_bullet, "space")

#Main game loop
while True:
	
	for enemy in enemies:
		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			#Move all enemies down
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			#Change enemy direction
			enemyspeed *= -1
		        #check the collision between bullet and the enemy
		if isCollision(bullet, enemy):
                                
                         #Reset the bullet
			 bullet.hideturtle()
			 bulletstate = "ready"
			 bullet.setposition(0,-200)
			 winsound.PlaySound("spacio.wav" , winsound.SND_ASYNC)
			 #Reset the enemy
			 x=random.randint(-200,200)
			 y=random.randint(100,250)
			 enemy.setposition(x,y)
			 #Update the score
			 score+=10
			 scorestring="Score:%s" %score
			 score_pen.clear()
			 score_pen.write(scorestring,False,align="left",font=("bold",18,"normal"))
			 
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()

			wn.bgpic("end.gif")
			#Sound if the player hit any of the enemy
			
			winsound.PlaySound("pacman_death.wav", winsound.SND_ASYNC)
			print ("Game Over")
			sys.exit()
			
			break
			
	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 290:
		bullet.hideturtle()
		bulletstate = "ready"
		
		
delay = raw_input("Press delete to finish.")

