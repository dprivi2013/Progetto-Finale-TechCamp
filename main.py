import pygame
from time import sleep
from random import randint
pygame.init()

#Sprite
bluedropimg= pygame.image.load('goccia blu.png')
blackdropimg=pygame.image.load('goccia nera.png')
greendropimg=pygame.image.load('goccia verde.png')
purpledropimg=pygame.image.load('goccia viola.png')
bluedropimg=pygame.transform.scale(bluedropimg, (20,30))
blackdropimg=pygame.transform.scale(blackdropimg,(20,30)) 
greendromimg=pygame.transform.scale(greendropimg, (20,30))
purpledropimg=pygame.transform.scale(purpledropimg, (20,30))


#Variabili
x = 0
y = 450
vx = 1
length = 50
height = 50
#drop = [x,y,velocità]
bluedrop = [randint(0,480),0,randint(10,30)/10]
blackdrop = [randint(0,480),0,randint(10,30)/10]
screen = pygame.display.set_mode((500,500))
pygame.draw.rect(screen, (0,0,0),(0,450,50,50))

def render():
  screen.fill((178,255,255))
  pygame.draw.rect(screen, (0,0,0),(x,y,length,height))
  #pygame.draw.circle(screen,(0,0,255),(drop1x,drop1y),dropr)
  bluedropfun()
  blackdropfun()
  screen.blit(bluedropimg, (bluedrop[0], bluedrop[1]))
  screen.blit(blackdropimg, (blackdrop[0], blackdrop[1]))
  pygame.display.flip()

def bluedropfun():
  global bluedrop
  bluedrop[1]=bluedrop[1]+bluedrop[2]
  if bluedrop[1]+30>500:
    bluedrop[1]=15
    bluedrop[0]=randint(0,470)
    
def blackdropfun():
  global blackdrop, dropr
  blackdrop[1]=blackdrop[1]+blackdrop[2]
  if blackdrop[1]+30>500:
    blackdrop[1]=15
    blackdrop[0]=randint(0,470)

def keys_handler():
  global x, vx
  pygame.event.get()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_LEFT]==1:
    x-=2
  if keys[pygame.K_RIGHT]==1:
    x+=2
  
def border():
  global x
  if x+length>500:
    x=500-length
  if x<0:
    x=0

while True:
  keys_handler()
  render()
  border()
  sleep(0.01)
