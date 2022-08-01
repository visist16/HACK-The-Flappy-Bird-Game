import pygame
from random import randint
pygame.init()
display = pygame.display.set_mode((320, 568))
text = pygame.font.Font(None, 50)
bg = pygame.image.load('bg.png')
bird = pygame.image.load('bird.png')
pole_width = 70
pole_gap = 100
pole_x = 320
top_pole_height = randint(100, 400)
pole_color = (220, 85, 57)
bird_x = 20
bird_y = top_pole_height + 20
score = 0
clock = pygame.time.Clock()

