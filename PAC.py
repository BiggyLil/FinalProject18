import pygame
background_colour = (0,0,0)

width, height = 400, 400
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('PACMAN')

pacImg = pygame.image.load('DOM.jpg')

x = (width*0.45)
y= (height*0.8)

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
  pygame.display.update()

  screen.fill(background_colour)
  car(x,y)
  
  pygame.display.flip()

def pac(x,y):
  gameDisplay.blit(pacImg,(x,y))

