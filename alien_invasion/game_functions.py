#! /usr/bin/python3
#-*-coding:utf-8-*-

'''
所有管理事件的代码
'''
import sys
import pygame

def check_events():
    #监视鼠标和键盘事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_setting,screen,ship):
    screen.fill(ai_setting.bg_color)
    ship.blitme() #绘制飞船
    pygame.display.flip()  #让绘制的屏幕可见
