'''
事件代码，
隔离事件，管理循环
归纳 alien_invasion，清晰代码逻辑
'''
import sys
import pygame


def check_events():
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    '''更新图像，并绘制到屏幕'''
    screen.fill(ai_settings.bg_color)
    ship.blitme()
