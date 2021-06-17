import pygame
from time import sleep
from random import randint
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Press Start 2P', 50)

#Sprite Gocce
bluedropimg= pygame.image.load('goccia blu.png')
blackdropimg=pygame.image.load('goccia nera.png')
greendropimg=pygame.image.load('goccia verde.png')
purpledropimg=pygame.image.load('goccia viola.png')
bluedropimg=pygame.transform.scale(bluedropimg, (20,30))
blackdropimg=pygame.transform.scale(blackdropimg,(20,30)) 
greendromimg=pygame.transform.scale(greendropimg, (20,30))
purpledropimg=pygame.transform.scale(purpledropimg, (20,30))

#Sprite Pianta
pianta0 = pygame.image.load("pianta0.png")
pianta1 = pygame.image.load("pianta1.png")
pianta2 = pygame.image.load("pianta2.png")
piantamorta = pygame.image.load("piantamorta.png")
pianta0 = pygame.transform.scale(pianta0, (70,70))
pianta1 = pygame.transform.scale(pianta1, (70,70))
pianta2 = pygame.transform.scale(pianta2, (70,70))
piantamorta = pygame.transform.scale(piantamorta, (70,70))

#Variabili
x = 0
y = 450
vx = 1
length = 50
height = 50
#drop = [x,y,velocità]
bluedrop = [randint(0,480),0,randint(10,30)/10]
blackdrop = [randint(0,480),0,randint(10,30)/10]
purpledrop = [randint(0,480),0,randint(10,30)/10]
screen = pygame.display.set_mode((500,500))
pygame.draw.rect(screen, (0,0,0),(0,450,50,50))
bluescore=0
blackscore=0
purplescore=0

def render():
  screen.fill((178,255,255))
  pygame.draw.rect(screen, (0,0,0),(x,y,length,height))
  #pygame.draw.circle(screen,(0,0,255),(drop1x,drop1y),drop)
  blue_score()
  bluedropfun()
  blackdropfun()
  purpledropfun()
  screen.blit(bluedropimg, (bluedrop[0], bluedrop[1]))
  screen.blit(blackdropimg, (blackdrop[0], blackdrop[1]))
  screen.blit(purpledropimg, (purpledrop[0], purpledrop[1]))
  screen.blit(pianta0, (x,y))
  print(str(bluescore))
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

def purpledropfun():
  global purpledrop
  purpledrop[1]=purpledrop[1]+purpledrop[2]
  if purpledrop[1]+30>500:
    purpledrop[1]=15
    purpledrop[0]=randint(0,470)

def blue_score():
  global bluescore
  if bluedrop[1]==450 and x-20<bluedrop[0] and bluedrop[0]<x+length:
    bluescore+=1
    bluedropfun()

def black_score():
  global blackscore
  if blackdrop[1]==450 and x-20<blackdrop[0] and blackdrop[0]<x+length:
    blackscore+=1

def purple_score():
  global purplescore
  if purpledrop[1]==450 and x-20<purpledrop[0] and purpledrop[0]<x+length:
    purplescore+=1

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
  blue_score()
  sleep(0.01)