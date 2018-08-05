#! /usr/bin/env python
#-*-coding: utf-8-*-

import pygame
import game_functions as gf
from ship import Ship
from settings import Settings
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width , ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion") #显示标题

    ship = Ship(screen) #创建一艘飞船
    while True:
        gf.check_events()
        gf.update_screen(ai_setting,screen,ship)
run_game()




