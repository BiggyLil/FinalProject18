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

ghost_h= 50
ghost_w= 50

dx= 700
dy= 300

pacman_w = 50
pacman_h = 50

lives=3

class Pacman(pygame.sprite.Sprite):
  """defines paccy"""
  def __init__(self):
    self.rect.x=0
    self.rect.y=0
    super.__init__()
    self.image= pygame.image.load('PAAAAAAAAAAAAACCCCCCCCCC.png')
    self.rect=self.image.get_rect()

  def display(self):
    screen.blit(pac, (px, py))
 
  def move(self):
   if event.type == pygame.KEYDOWN:
    if pygame.key.name(event.key) == 'up':
      self.rect.y-=1
    if pygame.key.name(event.key) == 'down':
      self.rect.y+=1
    if pygame.key.name(event.key) == 'right':
      self.rect.x+=1
    if pygame.key.name(event.key) == 'left':
      self.rect.x-=1

   if px < 0:
     px=0
   elif px > 800-pacman_w:
      px=800-pacman_w
   if py < 0:
      py=0
   elif py > 400-pacman_h:
     py=400-pacman_h

pac=Pacman()

class Ghosts(pygame.sprite.Sprite):
  """defines ghosties"""
  def __init__(self):
    self.rect.x = 50
    self.rect.y = 50
    super.__init__()
    if name== 'derbie':
      self.image= pygame.image.load('ghooooooooost.png')
    if name== 'dobe':
      self.image= pygame.image.load('omgggggggggg.png')
    if name== 'dobie':
      self.image= pygame.image.load('ahhhhhhhh.png')
    self.rect=self.image.get_rect()

  def display(self):
    screen.blit(self.image, (self.rect.x, self.rect.y))
 
  def move(self, Pacman):
    distx= Pacman.rect.x-self.rect.x
    disty= Pacman.rect.x-self.rect.y
    if random.random()<.02:
      self.rect.x+=distx/20
      self.rect.y+=disty/20

    if self.rect.x < 0:
      self.rect.x= 0
    elif self.rect.x > 800-ghost_w:
      self.rect.x= 800-ghost_w
    if self.rect.y < 0:
     self.rect.y= 0
    elif self.rect.y > 400-ghost_h:
      self.rect.y= 400-ghost_h

derbie= Ghosts()
dobe= Ghosts()
dobie =Ghosts()
 
class Dot(pygame.sprite.Sprite):
  """defines dot"""
  def __init__(self):
    self.rect.x= 700
    self.rect.y= 300
    super.__init__()
    self.image= pygame.image.load('dot.png')
    self.rect= self.image.get_rect()
  
  def display(self):
    screen.blit(self.image, (self.rect.x,self.rect.y))


running=True 

while running==True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  
  derbie.move()
  dobe.move()
  dobie.move()

  derbie.display()
  dobe.display()
  dobie.display()

  pac.display()
  pac.move()

  dot.display()

    # dx= random.randint(0,700)
    # dy= random.randint(0,300)

  pygame.display.flip()

