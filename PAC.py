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
ghostie = pygame.image.load('dom.png')

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(background_colour)
  
  screen.blit(ghostie, (s,n))
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
  
  pygame.display.flip()
