#!/usr/bin/env python
# -*-coding=utf-8-*-
"""
  > File Nmae :main.py
  > Author    : rack
  > Function  :
  > Github    : https://github.com/rack-leen
  > Date      : Thu 02 Aug 2018 08:30:18 PM CST
"""

import os
from card_linux import Project #导入目录中的模块

while 1 :
    card = Project()  #对象实例化
    card.print_page() #打印管理页

    try:
        func = int(input("请选择需要功能：")) #选择代表功能的数字，传入func
        os.system('clear') #linux下的清屏
        #os.system('clear') #windows清屏

        if func == 1 : #如果输入的是１
            card.print_page()
        elif func == 2 :
            card.add_card()
        elif func == 3 :
            card.delete_card()
        elif func == 4 :
            card.modify_card()
        elif func == 5 :
            card.find_card()
        elif func == 6 :
            card.display_card()
        elif func == 7 :
            card.save_mysql()
        elif func == 0 :
            card.quit_card()
    except ValueError:
        print("ValueError: 值错误，请重新输入选项!")


