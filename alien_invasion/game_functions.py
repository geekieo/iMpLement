'''
游戏所有事件代码，
隔离事件，管理循环
'''
import sys
import pygame
from bullet import Bullet

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


def update_screen(ai_settings, screen, ship, bullets, alien):
    '''将图像绘制到屏幕'''
    screen.fill(ai_settings.bg_color)
    # 在背景和飞船之间绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    alien.blitme()

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
