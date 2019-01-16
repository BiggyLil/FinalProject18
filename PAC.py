import pygame
import os
import random
pygame.init()

background_colour = (0,0,0)

width, height = 800, 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('PACMAN')

px=400
py=200

ghost_h= 88
ghost_w= 75

dx= 700
dy= 300

lives=3

class Ghosts:
  def __init__(self, name):
    self.name=name
    # self.image = ''
    self.x = 50
    self.y = 50
    if name== 'derbie':
      self.image= pygame.image.load('ghooooooooost.png')
    if name== 'dobe':
      self.image= pygame.image.load('omgggggggggg.png')
    if name== 'dobie':
      self.image= pygame.image.load('ahhhhhhhh.png')
  
  def display(self):
    screen.blit(self.image, (self.x, self.y))
 
  def move(self):
    distx= px-self.x
    disty= py-self.y
    if random.random()<.02:
      self.x+=distx/20
      self.y+=disty/20

    if self.x < 0:
      self.x= 0
    elif self.x > 800-ghost_w:
      self.x= 800-ghost_w
    if self.y < 0:
     self.y= 0
    elif self.y > 400-ghost_h:
      self.y= 400-ghost_h

derbie= Ghosts('derbie')
dobe= Ghosts('dobe')
dobie =Ghosts('dobie')

pac = pygame.image.load('PAAAAAAAAAAAAACCCCCCCCCC.png') 
  
running=True 

while running=True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  
  if event.type == pygame.KEYDOWN:
    if pygame.key.name(event.key) == 'up':
      py-=1
    if pygame.key.name(event.key) == 'down':
      py+=1
    if pygame.key.name(event.key) == 'right':
      px+=1
    if pygame.key.name(event.key) == 'left':
      px-=1
  
  derbie.move()
  dobe.move()
  dobie.move()

  derbie.display()
  dobe.display()
  dobie.display()
  

  screen.blit(pac, (px, py))
  pacman_w = 75
  pacman_h = 75
  if px < 0:
     px=0
  elif px > 800-pacman_w:
    px=800-pacman_w
  if py < 0:
    py=0
  elif py > 400-pacman_h:
    py=400-pacman_h

  dot= pygame.image.load('dot.png')

  def display_dot():
    screen.blit(dot, (dx,dy))
  
  display_dot()

  if px==dx and py==dy:
    dx= random.randint(0,700)
    dy= random.randint(0,300)

  pygame.display.flip()


