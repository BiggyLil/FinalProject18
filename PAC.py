import pygame
import os
import random
pygame.init()

background_colour = (0,0,0)

width, height = 400, 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('PACMAN')

x=0
y=0
s=0
n=0

pac = pygame.image.load('dom.png')

class Ghosts:
  def __init__(self, name):
    self.name=name

    def move(self):
       screen.blit(Ghosts, (s,n))
        s += random.randint(-5,5)
        n += random.randint(-5,5)
         if s < 0:
           s=400
         elif s > 400:
           s=0
          if n < 0:
            n=400
          elif n > 400:
            n=0

derbie= Ghosts('derbie')
dobe= Ghosts('dobe')
dobie =Ghosts('dobie')


derbie = pygame.image.load('derbie.png')
dobe = pygame.image.load('dobe.png')
dobie = pygame.image.load('dobie.png')

derbie.move()
dove.move()
dobie.move()

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  
  pygame.display.flip()
