#!/usr/bin/python3
import sys, pygame
pygame.init()
x = 1280
y = 780
size = width, height = x, y
green = 0, 128, 0
black = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Organ Trade 3000')
font = pygame.font.Font(None, 100)
text = font.render('Oregon Trail 3000', True, green)
textrect = text.get_rect()
textrect.center = (x // 2, y // 2)
while True:
    screen.fill(black)
    screen.blit(text, textrect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
