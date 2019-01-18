import pygame
import os
import random
pygame.init()

background_colour = (0,0,0)

s_width = 1300
s_height = 600
screen = pygame.display.set_mode((s_width, s_height))

pygame.display.set_caption("PACMAN BUT BETTER")

ghost_h= 50
ghost_w= 50

pacman_w = 50
pacman_h = 50

all_sprites= pygame.sprite.Group()

lives=3

points=0

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
   elif self.rect.x > s_width - pacman_w - 100:
      self.rect.x= s_width - pacman_w - 100
   if self.rect.y < 0:
      self.rect.y = 0
   elif self.rect.y > s_height - pacman_h - 100:
     self.rect.y= s_height - pacman_h - 100

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

  def update(self, Pacman):
    distx= Pacman.rect.x-self.rect.x
    disty= Pacman.rect.y-self.rect.y
    if random.random()<.02:
      self.rect.x+=distx/20
      self.rect.y+=disty/20

    if self.rect.x < 0:
      self.rect.x = 0
    elif self.rect.x > s_width - ghost_w - 100:
      self.rect.x= s_width - ghost_w - 100
    if self.rect.y < 0:
     self.rect.y= 0
    elif self.rect.y > s_height - ghost_h - 100:
      self.rect.y= s_height - ghost_h - 100

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
      self.rect.x= random.randint(0,s_width-100)
      self.rect.y= random.randint(0,s_height-100)
 
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
  if pygame.sprite.collide_rect(pac, dot):
    dot.update()
    points+=10

  # if pygame.sprite.collide_rect(pac, ghost_list):
  #   lives-=1

  if lives<0:
    break

  pygame.display.flip()

gameover= pygame.image.load("Game Over Screen.jpg")
screen.blit(gameover, (400, 200))