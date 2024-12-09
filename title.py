#!/usr/bin/python3
import pygame
pygame.init()
x = 1280
y = 780
size = width, height = x, y
green = 0, 128, 0
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Organ Trade 3000')
font = pygame.font.Font(None, 100)
start_size = pygame.font.Font(None, 32)
text = font.render('Oregon Trail 3000', True, green)
start = start_size.render('Press a button to start', True, green)
textrect = text.get_rect()
start_rect = start.get_rect()
textrect.center = (x // 2, y // 2)
start_rect.center = (x // 2, y // 2 + 100)
while True:
    screen.fill(black)
    screen.blit(text, textrect)
    screen.blit(start, start_rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
