import pygame
import os
import random
import time

pygame.init()

Clock = pygame.time.Clock()

black = (0,0,0)

white = (255,255,255)

gray = (169,169,169)

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

welcome= pygame.image.load("intro screen.jpg")
gameover= pygame.image.load("Game Over Screen.jpg")

class Pacman(pygame.sprite.Sprite):
  """defines paccy"""
  def __init__(self):
    super().__init__()
    self.image= pygame.image.load('PAAAAAAAAAAAAACCCCCCCCCC.png')
    self.rect=self.image.get_rect()
    self.rect.x=650
    self.rect.y=100
    #may need to change this later

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
    self.rect.x = 650
    self.rect.y = 500
    #may need to change this

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
    self.rect.x= s_width/2
    self.rect.y= s_height/2
  
  def display(self):
    screen.blit(self.image, (self.rect.x,self.rect.y))

  def update(self):
      self.rect.x= random.randint(0,s_width-100)
      self.rect.y= random.randint(0,s_height-100)
 
dot= Dot()
all_sprites.add(dot)

def text_objects(text, font, color):
  textSurface= font.render (text, True, color)
  return textSurface, textSurface.get_rect()

def message_display(text, color, x, y, size):
  Text = pygame.font.Font('freesansbold.ttf', size)
  TextSurf, TextRect = text_objects(text, Text, color)
  TextRect.center = (x,y)
  screen.blit(TextSurf, TextRect)
  pygame.display.update()

def button (msg, x, y, w, h, mon, moff, tc, ts):
    mouse =  pygame.mouse.get_pos()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
      pygame.draw.rect(screen, mon, (x,y,w,h))
    else:
      pygame.draw.rect(screen, moff, (x,y,w,h))

    message_display(msg, tc, (x+(w/2)), (y+(h/2)), ts)

def game_intro():
  intro =  True
  while intro:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
    screen.blit(welcome, (0,0))
    
    message_display("PACMAN(2.0)", white, s_width/2, 100, 115)

    button("START", 515, 200, 300, 50, gray, white, black, 50)

    pygame.display.flip()
    Clock.tick(5)
 
running=True 

while running==True:
  game_intro()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(black)

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
screen.blit(gameover, (400, y))