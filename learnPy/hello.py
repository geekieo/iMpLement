#!/usr/bin/env python
import pygame

image = pygame.image.load('ship.bmp')
screen=pygame.display.set_mode((800,600))
screen.blit(image,(300,200))
#显示画面
pygame.display.flip()
