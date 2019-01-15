import pygame
import os
import random
pygame.init()

background_colour = (0,0,0)

width, height = 800, 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('PACMAN')

x=0
y=0

ghost_h= 100
ghost_w= 100

class Ghosts:
  def __init__(self, name):
    self.name=name
    # self.image = ''
    self.x = 50
    self.y = 50
    if name== 'derbie':
      self.image= pygame.image.load('derbie.png')
    if name== 'dobe':
      self.image= pygame.image.load('dobe.png')
    if name== 'dobie':
      self.image= pygame.image.load('dobie.png')
  
  def display(self):
    screen.blit(self.image, (self.x, self.y))
  def move(self):
    
    self.x += random.randint(-5,5)
    self.y += random.randint(-5,5)
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

pac = pygame.image.load('dom.png') 


running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  
  if event.type == pygame.KEYDOWN:
    if pygame.key.name(event.key) == 'up':
      y-=5
    if pygame.key.name(event.key) == 'down':
      y+=5
    if pygame.key.name(event.key) == 'right':
      x+=5
    if pygame.key.name(event.key) == 'left':
      x-=5

  derbie.move()
  dobe.move()
  dobie.move()

  derbie.display()
  dobe.display()
  dobie.display()
  

  screen.blit(pac, (x, y))
  pacman_w = 100
  pacman_h = 100
  if x < 0:
     x=0
  elif x > 800-pacman_w:
    x=800-pacman_w
  if y < 0:
    y=0
  elif y > 400-pacman_h:
    y=400-pacman_h

  pygame.display.flip()



