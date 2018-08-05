#! /usr/bin/python3
#-*-coding:utf-8-*-
import pygame

class Ship():
    def __init__(self,screen):
        self.screen = screen

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect() #飞船外接矩形
        self.screen_rect = screen.get_rect()#屏幕矩形

        self.rect.centerx = self.screen_rect.centerx #屏幕矩形中央赋值给飞船矩形中央
        self.rect.bottom = self.screen_rect.bottom #屏幕矩形底部赋值给飞船矩形底部

    def blitme(self):
        self.screen.blit(self.image,self.rect) #绘制飞船
