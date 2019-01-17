import pygame
import os
import random
pygame.init()

background_colour = (0,0,0)

width, height = 800, 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("PACMAN BUT BETTER")

ghost_h= 50
ghost_w= 50

pacman_w = 50
pacman_h = 50

all_sprites= pygame.sprite.Group()

lives=3

class Pacman(pygame.sprite.Sprite):
  """defines paccy"""
  def __init__(self):
    super().__init__()
    self.image= pygame.image.load('PAAAAAAAAAAAAACCCCCCCCCC.png')
    self.rect=self.image.get_rect()
    self.rect.x=0
    self.rect.y=0

  def display(self):
    screen.blit(self.image, (self.rect.x, self.rect.y))
 
  def update(self):
   if event.type == pygame.KEYDOWN:
    if pygame.key.name(event.key) == 'up':
      self.rect.y-=1
    if pygame.key.name(event.key) == 'down':
      self.rect.y+=1
    if pygame.key.name(event.key) == 'right':
      self.rect.x+=1
    if pygame.key.name(event.key) == 'left':
      self.rect.x-=1

   if self.rect.x < 0:
     self.rect.x=0
   elif self.rect.x > 800-pacman_w:
      self.rect.x=800-pacman_w
   if self.rect.y < 0:
      self.rect.y=0
   elif self.rect.y > 400-pacman_h:
     self.rect.y=400-pacman_h

pac=Pacman()
all_sprites.add(pac)

class Ghosts(pygame.sprite.Sprite):
  """defines ghosties"""
  def __init__(self, name):
    super().__init__()
    if name== 'derbie':
      self.image= pygame.image.load('ghooooooooost.png')
    if name== 'dobe':
      self.image= pygame.image.load('omgggggggggg.png')
    if name== 'dobie':
      self.image= pygame.image.load('ahhhhhhhh.png')
    self.rect=self.image.get_rect()
    self.rect.x = 50
    self.rect.y = 50

  # def display(self):
  #   screen.blit(self.image, (self.rect.x, self.rect.y))
 

  def update(self, Pacman):
    distx= Pacman.rect.x-self.rect.x
    disty= Pacman.rect.y-self.rect.y
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

derbie= Ghosts('derbie')
dobe= Ghosts('dobe')
dobie =Ghosts('dobie')

ghost_list= pygame.sprite.Group()
ghost_list.add(Ghosts('derbie'))
ghost_list.add(Ghosts('dobe'))
ghost_list.add(Ghosts("dobie"))
 
class Dot(pygame.sprite.Sprite):
  """defines dot"""
  def __init__(self):
    super().__init__()
    self.image= pygame.image.load('dot.png')
    self.rect= self.image.get_rect()
    self.rect.x= 700
    self.rect.y= 300
  
  def display(self):
    screen.blit(self.image, (self.rect.x,self.rect.y))

  def update(self):
      self.rect.x= random.randint(0,700)
      self.rect.y= random.randint(0,300)
 
dot= Dot()
all_sprites.add(dot)

running=True 

while running==True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)

  ghost_list.update(pac)
  ghost_list.draw(screen)

  pac.display()
  pac.update()

  dot.display()
  dot.update(pac)

  pygame.display.flip()

