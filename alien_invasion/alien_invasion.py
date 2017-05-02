#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gameFunc
from pygame.sprite import Group


def run_game():

    # 初始化游戏并创建屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人
    alien = Alien(ai_settings, screen)

    # 开始游戏主循环
    while True:
        gameFunc.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gameFunc.update_bullets(bullets)
        gameFunc.update_screen(ai_settings, screen, ship, bullets, alien)
        pygame.display.flip()
        # 延迟执行下一循环
        pygame.time.delay(10)


run_game()
