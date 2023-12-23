# classic pong game
try:
    from ursina import *
except ImportError:
    import pip
    pip.main(['install', 'ursina'])
    from ursina import *

import random
import math



app = Ursina()

window.color = color.black
window.title = 'Pong'
window.borderless = False
window.exit_button.visible = False
window.fullscreen = False
window.size = (800, 600)
# uses background.png located in assets/background.png as background
background = Entity(model='quad', texture='background', scale=(14, 8.8), z=1)

scoreleft = 0
scoreright = 0

scoreText = Text(text=str(scoreleft) + " | " + str(scoreright), scale=2, position=(0, 0.5), color=color.white)


paddleLeft = Entity(model='quad', color=color.white, scale=(0.1, 1), position=(-6, 0))
paddleRight = duplicate(paddleLeft, x=6)
ball = Entity(model='circle', color=color.white, scale=0.1, position=(0, 0))

velocityX = 3
velocityY = 3

def updateScore():
    scoreText.text = str(scoreleft) + " | " + str(scoreright)

def resetVelocity():
    global velocityX, velocityY
    velocityX = 3
    velocityY = 3

def update():
    
    global velocityX, velocityY, scoreleft, scoreright

    if held_keys['w']:
        paddleLeft.y += 3 * time.dt
    if held_keys['s']:
        paddleLeft.y -= 3 * time.dt
    if held_keys['up arrow']:
        paddleRight.y += 3 * time.dt
    if held_keys['down arrow']:
        paddleRight.y -= 3 * time.dt

    ball.x += velocityX * time.dt
    ball.y += velocityY * time.dt

    if ball.x > 6.1:
        ball.x = 0
        ball.y = 0
        scoreleft += 1
        updateScore()
        resetVelocity()
    if ball.x < -6.1:
        ball.x = 0
        ball.y = 0
        scoreright += 1
        resetVelocity()
        updateScore()

    
    if ball.y > 4:
        velocityY = -1*(velocityY)
    if ball.y < -4:
        velocityY = -1*(velocityY)

    if (ball.x-0.1) <= paddleLeft.x and (ball.y>=paddleLeft.y-0.5 and ball.y<=paddleLeft.y+0.5):
        velocityX = -1*(velocityX)
        velocityY= -1*(velocityY)
        velocityX+=random.random()
        velocityY+=random.random()
    if (ball.x+0.1) >= paddleRight.x and (ball.y>=paddleRight.y-0.5 and ball.y<=paddleRight.y+0.5):
        velocityX = -1*(velocityX)
        velocityY = -1*(velocityY)
        velocityX-=random.random()
        velocityY-=random.random()
        
    if paddleLeft.y > 3.6:
        paddleLeft.y = 3.6
    if paddleLeft.y < -3.6:
        paddleLeft.y = -3.6
    if paddleRight.y > 3.6:
        paddleRight.y = 3.6
    if paddleRight.y < -3.6:
        paddleRight.y = -3.6

app.run()

while True:
    update()