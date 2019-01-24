import pygame
import os
import random
import time

pygame.init()

Clock = pygame.time.Clock()

black = (0,0,0)

white = (255,255,255)

gray = (169,169,169)
# colors

s_width = 1300
s_height = 600
screen = pygame.display.set_mode((s_width, s_height))
#screen width and height

pygame.display.set_caption("PACMAN BUT BETTER")
#display caption

ghost_h= 50
ghost_w= 50
#ghost height and width

pacman_w = 50
pacman_h = 50
#pacman's height and width

all_sprites= pygame.sprite.Group()

points=0

dotcontact=0
#^number of times pac has touced pac

level=int()
#default number of points level, and dotcontact

welcome= pygame.image.load("intro screen.jpg")
gameover= pygame.image.load("Game Over Screen.jpg")
#images for intro and game over screens

class Pacman(pygame.sprite.Sprite):
  """defines pacman"""
  def __init__(self):
    super().__init__()
    self.image= pygame.image.load('PAAAAAAAAAAAAACCCCCCCCCC.png')
    self.rect=self.image.get_rect()
    self.rect.x=0
    self.rect.y=0
    #^pac's starting position & image

  def display(self):
    """displays pacman"""
    screen.blit(self.image, (self.rect.x, self.rect.y))
 
  def update(self):
    """makes pacman move"""
    if event.type == pygame.KEYDOWN:
      if pygame.key.name(event.key) == 'up':
        self.rect.y-=5
      if pygame.key.name(event.key) == 'down':
        self.rect.y+=5
      if pygame.key.name(event.key) == 'right':
        self.rect.x+=5
      if pygame.key.name(event.key) == 'left':
        self.rect.x-=5
#creates boundaries for pacman"""
    if self.rect.x < 0:
      self.rect.x=0
    elif self.rect.x > s_width-pacman_w-100:
      self.rect.x=s_width-pacman_w-100
    if self.rect.y < 0:
      self.rect.y=0
    elif self.rect.y > s_height-pacman_w-100:
      self.rect.y= s_height-pacman_w-100

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
    self.rect.x = 1100
    self.rect.y = 200
# ghosts' starting position & image

  def update(self, Pacman,num):
    """makes ghosts move"""
    distx= Pacman.rect.x-self.rect.x
    disty= Pacman.rect.y-self.rect.y
    if random.random()<.02:
      self.rect.x+=distx/num
      self.rect.y+=disty/num

    if self.rect.x < 0:
      self.rect.x = 0
    elif self.rect.x > s_width - ghost_w - 100:
      self.rect.x= s_width - ghost_w - 100
    if self.rect.y < 0:
     self.rect.y= 0
    elif self.rect.y > s_height - ghost_h - 100:
      self.rect.y= s_height - ghost_h - 100
#creates boundaries for ghosts

derbie= Ghosts('derbie')
dobe= Ghosts('dobe')
dobie =Ghosts('dobie')

ghost_list= pygame.sprite.Group()
ghost_list.add(Ghosts('derbie'))
ghost_list.add(Ghosts('dobe'))
ghost_list.add(Ghosts('dobie'))
 
class Dot(pygame.sprite.Sprite):
  """defines dot"""
  def __init__(self):
    super().__init__()
    self.image= pygame.image.load('dot.png')
    self.rect= self.image.get_rect()
    self.rect.x= s_width/2
    self.rect.y= s_height/2
#dot image and starting position
  
  def display(self):
    """displays dot image"""
    screen.blit(self.image, (self.rect.x,self.rect.y))

  def update(self):
    """makes the dot appear in random locations on the screen"""
    self.rect.x= random.randint(0,s_width-150)
    self.rect.y= random.randint(0,s_height-150)
 
dot= Dot()
all_sprites.add(dot)

def text_objects(text, font, color):
  """defines text objects"""
  textSurface= font.render (text, True, color)
  return textSurface, textSurface.get_rect()

def message_display(text, color, x, y, size):
  """Allows for text to be displayed a certain location with a certain color and size"""
  Text = pygame.font.Font('freesansbold.ttf', size)
  TextSurf, TextRect = text_objects(text, Text, color)
  TextRect.center = (x,y)
  screen.blit(TextSurf, TextRect)

def button (msg, x, y, w, h, mon, moff, tc, ts):
  """creates a button function"""
  mouse =  pygame.mouse.get_pos()

  if x+w > mouse[0] > x and y+h > mouse[1] > y:
    pygame.draw.rect(screen, mon, (x,y,w,h))
        
  else:
    pygame.draw.rect(screen, moff, (x,y,w,h))

  message_display(msg, tc, (x+(w/2)), (y+(h/2)), ts)
#button changes color when hovered upon & displays text

intro_mode= True

def game_intro():
  """displays game intro"""
  global intro_mode
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
  
  screen.blit(welcome, (0,0))
  
  message_display("PACMAN(2.0)", white, s_width/2, 100, 115)

  button("START", 515, 200, 300, 50, gray, white, black, 50)
  
  if 515+300 > pygame.mouse.get_pos()[0] > 515 and 200+50 > pygame.mouse.get_pos()[1] > 200:
    if pygame.MOUSEBUTTONDOWN:
      intro_mode= False

  pygame.display.flip()
    
  Clock.tick(5)
# intro screen displays welcome image and text along with button
 
def game_over():
  """displays game over screen"""
  global points
  global dotcontact

  lost = True
  while lost==True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()

    screen.blit(gameover, (0,0))
# game over image
    button("EXIT", 325, 320, 300, 50, gray, white, black, 50)
    button("PLAY AGAIN", 650, 320, 300, 50, gray, white, black, 40)
#exit and play again buttons
    if 325+300 >  pygame.mouse.get_pos()[0] > 325 and 320+50 >  pygame.mouse.get_pos()[1] > 320:
      if pygame.MOUSEBUTTONDOWN:
        pygame.quit()
#when exit button is pushed, the game is exited
    if 650+300 >  pygame.mouse.get_pos()[0] > 650 and 320+50 >  pygame.mouse.get_pos()[1] > 320:
      if pygame.MOUSEBUTTONDOWN:
        intro_mode= True
        lost = False
        pac.rect.x= 0
        pac.rect.y= 0
        for ghost in ghost_list:
          ghost.rect.x= 1100
          ghost.rect.y= 200
        points= 0
        dotcontact=0
        dot.rect.x= s_width/2
        dot.rect.y= s_height/2
#when 'play again' button is pushed, the game restarts and everything is reset

    pygame.display.flip()
    Clock.tick(5)

running = True 

while running == True:
  """main loop"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  while intro_mode== True:
    game_intro()

  screen.fill(black)

  ghost_list.draw(screen)

  pac.display()
  pac.update()

  dot.display()

  if pygame.sprite.collide_rect(pac, dot):
    dot.update()
    dotcontact+=1
    if 0<dotcontact<4:
      level=1
    elif 3<dotcontact<7:
      level=2
      points+=50
    elif 6<dotcontact<10:
      level=3
      points+=100
    else:
      game_over()
# dot is at new location, level is increased, and game ends once the last level is passed

  if level==1:
    ghost_list.update(pac, 20)
  if level==2:
    ghost_list.update(pac, 10)
  else:
    ghost_list.update(pac, 5)
# ghosts increase in speed when new levels are reached

  if pygame.sprite.spritecollideany(pac, ghost_list):
    game_over()
# game ends if pacman touches ghosts
    
  message_display("Points:", white, 1230, 50, 20)
  message_display(f"{points}", white, 1230, 80, 20)
  message_display(f"Level:{level}", white, 325, 560, 50)
  message_display(f"You have one life, bud...JUST ONE", white, 975, 560, 30)
#displays number of points left, level, and that lives=1

  print (intro_mode)

  pygame.display.flip()



