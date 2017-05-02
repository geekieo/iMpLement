'''
游戏所有事件代码，
隔离事件，管理循环
'''
import sys
import pygame
from bullet import Bullet
from alien import Alien

# 长按退出倒计时
PRESS_WAITING_TIME = 2000
# 计时列表
time_start = {}


def timing(event, time_start):
    '''长按esc计时退出'''
    time_end = time_start['esc'] + PRESS_WAITING_TIME
    time_now = pygame.time.get_ticks()
    while event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        time_now = pygame.time.get_ticks()
        if time_now > time_end:
            sys.exit()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_ESCAPE:
        esc_time_start = pygame.time.get_ticks()
        time_start['esc'] = esc_time_start
        timing(event, time_start)


def check_keyup_events(event, ship):
    '''响应按键松开'''
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets, aliens):
    '''将图像绘制到屏幕'''
    screen.fill(ai_settings.bg_color)
    # 在背景和飞船之间绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    for alien in aliens.sprites():
        alien.draw_alien()
    # aliens.draw(screen)


def update_bullets(bullets):
    '''更新子弹位置，并删除消失子弹'''
    # 更新子弹位置
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    # print(len(bullets))


def fire_bullet(ai_settings, screen, ship, bullets):
    '''子弹数量未达到限制，就创建一颗子弹'''
    # 创建一个子弹， 并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_aliens_cols(ai_settings, alien_width):
    '''计算屏幕一行可容纳多少个外星人'''
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_cols = int(available_space_x / (2 * alien_width))
    return number_cols


def get_aliens_rows(ai_settings, ship_height, alien_height):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_cols, alien_rows):
    # 创建一个外星人并加入当前行
    alien = Alien(ai_settings, screen)

    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_cols  # x轴坐标
    alien.rect.x = alien.x

    alien_height = alien.rect.height
    alien.y = alien_height + 2 * alien_height * alien_rows
    alien.rect.y = alien.y

    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    '''创建外星人群'''
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    aliens_cols = get_aliens_cols(ai_settings, alien.rect.width)
    aliens_rows = get_aliens_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    for alien_rows in range(aliens_rows):
        # 创建一行外星人
        for alien_cols in range(aliens_cols):
            create_alien(ai_settings, screen, aliens, alien_cols, alien_rows)
