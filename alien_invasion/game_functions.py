'''
游戏所有事件代码，
隔离事件，管理循环
'''
import sys
from time import sleep

import pygame

from alien import Alien
from bullet import Bullet


class GameFunctions ():

    def __init__(self):
        # 计时列表
        self.time = {}
        self.press_esc = False
        self.aliens_empty = False
        self.ship_dead = False

    def check_keydown_events(self, event, ai_settings, screen, ship, bullets):
        '''响应按键按下'''
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_UP:
            ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet(ai_settings, screen, ship, bullets)
        elif event.key == pygame.K_ESCAPE:
            self.time['esc'] = pygame.time.get_ticks()
            self.press_esc = True

    def check_keyup_events(self, event, ship):
        '''响应按键松开'''
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False
        elif event.key == pygame.K_UP:
            ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            ship.moving_down = False
        elif event.key == pygame.K_ESCAPE:
            self.press_esc = False

    def check_events(self, ai_settings, screen, ship, bullets, aliens, play_button, stats):
        '''响应按键和鼠标事件'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(
                    event, ai_settings, screen, ship, bullets)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event, ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_play_button(
                    ai_settings, screen, stats, play_button, mouse_x, mouse_y, ship, bullets, aliens)

    def check_play_button(self, ai_settings, screen, stats, play_button, mouse_x, mouse_y, ship, bullets, aliens):
        '''玩家单击Play按钮开始新的游戏'''
        if play_button.rect.collidepoint(mouse_x, mouse_y):
            # 重置游戏统计信息
            stats.reset_stats()
            # 设置游戏状态为活动
            stats.game_active = True
            aliens.empty()
            bullets.empty()
            self.create_fleet(ai_settings, screen, aliens, ship)
            ship.center_ship()

    def update_press_timing(self, ai_settings):
        '''计时程序'''
        # 长按esc退出
        if self.press_esc == True:
            time_now = pygame.time.get_ticks()
            timing = time_now - self.time['esc']
            if timing >= ai_settings.press_waiting_time:
                sys.exit()

    def update_fleet_timing(self, ai_settings, screen, ship, bullets, aliens):
        # 删除所有子弹并新建一群外星人
        if self.aliens_empty == True:
            # 等待一段时间刷新新外星人
            time_now = pygame.time.get_ticks()
            timing = time_now - self.time['aliens_empty']
            if timing >= ai_settings.update_fleet_waiting_time:
                bullets.empty()
                self.create_fleet(ai_settings, screen, aliens, ship)
                self.aliens_empty = False

    def update_screen(self, ai_settings, screen, ship, bullets, aliens, stats, play_button):
        '''将图像绘制到屏幕'''
        screen.fill(ai_settings.bg_color)
        # 在背景和飞船之间绘制所有子弹
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        # for alien in aliens.sprites():
        #     alien.draw_alien()
        aliens.draw(screen)
        # 如果游戏为非活动状态，添加开始游戏的按钮
        if not stats.game_active:
            play_button.draw_button()
        pygame.display.flip()

    def update_bullets(self, bullets, aliens):
        '''更新子弹位置，并删除消失子弹'''
        # 更新子弹位置
        bullets.update()
        # 删除消失的子弹
        for bullet in bullets:
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # 检查 bullet 是否击中 alien
        # group 和 group 是否碰撞
        # 表示若rect重叠，则删除 bullet 和 alien，True，True表示两个都删除    ·
        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    def fire_bullet(self, ai_settings, screen, ship, bullets):
        '''子弹数量未达到限制，就创建一颗子弹'''
        # 创建一个子弹， 并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullet_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

    def get_aliens_cols(self, ai_settings, alien_width):
        '''计算屏幕一行可容纳多少个外星人'''
        available_space_x = ai_settings.screen_width - 2 * alien_width
        number_cols = int(available_space_x / (2 * alien_width))
        return number_cols

    def get_aliens_rows(self, ai_settings, ship_height, alien_height):
        '''计算屏幕可容纳多少行外星人'''
        available_space_y = (ai_settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = int(available_space_y / (2 * alien_height))
        return number_rows

    def create_alien(self, ai_settings, screen, aliens, alien_cols, alien_rows):
        # 创建外星人，并更具行列数设置坐标，存入aliens
        alien = Alien(ai_settings, screen)

        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_cols  # x轴坐标
        alien.rect.x = alien.x

        alien_height = alien.rect.height
        alien.y = alien_height + 2 * alien_height * alien_rows
        alien.rect.y = alien.y

        aliens.add(alien)

    def create_fleet(self, ai_settings, screen, aliens, ship):
        '''创建外星人群'''
        # 创建一个外星人，并计算一行可容纳多少个外星人
        # 外星人间距为外星人宽度
        alien = Alien(ai_settings, screen)
        aliens_cols = self.get_aliens_cols(ai_settings, alien.rect.width)
        aliens_rows = self.get_aliens_rows(
            ai_settings, ship.rect.height, alien.rect.height)

        for alien_rows in range(aliens_rows):
            # 创建一行外星人
            for alien_cols in range(aliens_cols):
                self.create_alien(ai_settings, screen, aliens,
                                  alien_cols, alien_rows)

    def check_fleet_edges(self, ai_settings, aliens):
        '''任意外星人到达边缘，移动方向改编'''
        for alien in aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction(ai_settings, aliens)
                break

    def change_fleet_direction(self, ai_settings, aliens):
        '''将所有外星人下移，并改变运动方向'''
        for alien in aliens.sprites():
            alien.rect.y += ai_settings.fleet_drop_speed_factor
        ai_settings.fleet_direction *= -1

    def ship_hit(self, ship, stats):
        '''响应被外星人撞到的飞船'''
        if stats.ships_left > 0:
            # 将 ships_left 减 1
            stats.ships_left -= 1
            # 创建新飞船
            ship.center_ship()
            ship_dead = True
        else:
            stats.game_active = False

    def check_aliens_bottom(self, screen, aliens, stats):
        '''检测外星人是否到达屏幕底端'''
        screen_rect = screen.get_rect()
        if stats.ships_left > 0:
            # 删除到达底部的外星人
            for alien in aliens:
                if alien.rect.bottom >= screen_rect.bottom:
                    aliens.remove(alien)
                    # 将 ships_left 减 1
                    stats.ships_left -= 1
        else:
            stats.game_active = False

    def update_aliens(self, ai_settings, screen, ship, bullets, aliens, stats):
        '''更新所有外星人的位置'''
        self.check_fleet_edges(ai_settings, aliens)
        aliens.update()
        if len(aliens) == 0 and self.aliens_empty == False:
            # 设置两个标记位，异或状态获取等待起始时间
            self.aliens_empty = True
            self.time['aliens_empty'] = pygame.time.get_ticks()
        # 检测外星人和飞船之间的碰撞，sprite 和 group 是否碰撞
        if pygame.sprite.spritecollideany(ship, aliens):
            # 删除撞到的外星人，不会删除飞船
            collisions = pygame.sprite.spritecollide(ship, aliens, True)
            self.ship_hit(ship, stats)
        # 检测外星人是否到达屏幕底端
        self.check_aliens_bottom(screen, aliens, stats)
