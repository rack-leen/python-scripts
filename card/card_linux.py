#!/usr/bin/env python
# -*-coding=utf-8-*-
"""
  > File Nmae :self.py
  > Author    : rack
  > Function  :
  > Github    : https://github.com/rack-leen
  > Date      : Thu 26 Jul 2018 05:46:20 PM CST

"""

"""
名片管理系统

提示用户内容
添加用户
删除名片
修改名片内容
查询名片内容
显示所有用户名片
退出管理系统
"""

import os #导入清屏命令
from mysql_card import Card_Mysql #从项目目录导入模块


class Project:
    """
    是名片管理系统的类定义，这个类中包含多个函数实现
    其中有需要实现的功能函数
    1. print_page   :  打印名片管理系统的主界面
    2. add_card     :  实现添加用户名片的功能
    3. delete_card  :  实现删除用户，名片的功能
    4. modify_card  :  实现修改用户名片
    5. find_card    :  查询需要的用户名片中的内容
    6. display_card :  显示所有的用户名片
    7. save_mysql   :  将所有的名片保存到数据库
    0. quit_card    :  退出名片管理系统

    以及其他辅助函数
    a. card_dict       :  字典信息赋值
    b. find_print   :  打印查询方式，作为查询方式的主界面
    """

    def __init__(self,names = 0 , ages = 0 , phone = 0 , address = 0 , card_imformation = {} , lists = []) :
        """
        self代表类实例本身
        下面的操作是将各个属性绑定到self
        names,ages,address --- 变量,用于输入用户信息
        card_imformation   --- 字典,是用来保存各个用户的名片信息
        lists              --- 列表,是许多字典的组合成的列表
        """
        self.names = names
        self.ages = ages
        self.phone = phone
        self.address = address
        self.card_imformation = card_imformation
        self.lists = lists


    # 为字典添加元素
    def card_dict(self):
        """
        a. card_dict --- 添加需要的字典信息
        """
        self.card_imformation = {"姓名":self.names , "年龄":self.ages ,"电话号码":self.phone , "家庭住址":self.address}
    #打印查询方式

    def find_print(self):
        """
        b. find_card --- 打印查询方式的界面
        """
        print("\t\t查询方式")
        print("====================================================")
        print("\t\t1. 姓名查询.")
        print("\t\t2. 年龄查询.")
        print("\t\t3. 索引值查询.")
        print("\t\t4. 家庭地址查询.")
        print("\t\t0. 退出查询.")
        print("====================================================")


    def print_page(self):
        """
        1. print_page --- 打印管理界面
        """
        #os.system('clear')
        print("====================================================")
        print("\t\t名片管理系统v8.0")
        print("====================================================")
        print("\n")
        print("\t\t名片管理页面")
        print("====================================================")
        print("\t\t1. 名片管理页面.")
        print("\t\t2. 添加用户名片.")
        print("\t\t3. 删除用户名片.")
        print("\t\t4. 修改用户名片内容.")
        print("\t\t5. 查询用户名片内容.")
        print("\t\t6. 显示所有用户名片.")
        print("\t\t7. 保存用户名片到数据库.")
        print("\t\t0. 退出名片管理系统.")
        print("====================================================")
    # 添加用户名片
    def add_card(self):
        """
        2. add_card --- 添加用户名片
        添加方式 --- 输入姓名年龄与家庭住址
        结束方式 --- 如果没有输入用户名，则以end结束（输入用户名之后，其他可以为空）
        """
        os.system('clear')
        self.display_card()
        while True :
            try:
                self.names = input("请输入添加的用户姓名,end结束：")
                if self.names == "end" :
                    break
                elif self.names == '' :
                    print("Error: 输入为空，姓名不存在！")
                self.ages = int(input("请输入添加的用户年龄(输入数字),end结束："))
                if self.ages == "end" :
                    break
                elif self.ages == '' :
                    print("Error: 输入为空，年龄不存在!")
                self.phone = input("请输入添加的用户电话号码(可以有字符),end结束：")
                if self.phone == "end" :
                    break
                elif self.phone == '' :
                    print("Error: 输入为空，电话号码不存在!")
                self.address = input("请输入添加的用户家庭住址,end结束：")
                if self.address == "end" : #如果输入的是end则结束添加
                # os.system('clear')
                    break
                elif self.address == '': #如果输入为空则返回错误
                    print("Error: 输入为空，家庭地址不存在!")
                else :
                    self.card_dict() #调用字典函数，得到字典信息
                    self.lists.append(self.card_imformation) #将输入的用户信息用字典表示并增加到列表中
            except ValueError:
                print("Error:值错误,只能输入数字!")


    # 删除用户名片
    def delete_card(self):
        """
        3. delete_card --- 删除用户名片
        删除方式    --- 用户名删除,end结束
        """
        os.system('clear')
        self.display_card()
        while True :
            self.names = input("请输入删除的用户姓名,end结束：")
            if self.names == "end" : #如果输入的是end则结束循环
            # os.system('clear')
                break
            else :
                try:
                    for dicts in self.lists : #遍历列表,dicts为列表中各个字典下标
                        if dict(dicts)['姓名'] == self.names : #需要删除的用户姓名与第dicts个字典中的姓名键对应的键值相等
                            self.lists.pop(self.lists.index(dicts)) #括号里面的是对应的字典所在的索引号，外面则是删除对应索引的字典
                except ValueError:
                    print("Error: 输入值错误，输入的不是有效用户!")

    # 修改名片内容
    def modify_card(self):
        """
        4. modify_card --- 修改名片内容
        修改方式       --- 确定需要修改的用户名，再输入修改后的用户信息
        """
        os.system('clear')
        self.display_card()
        while True :
            self.names = input("请输入需要修改的名片(用户名),end结束:")
            if self.names == "end" :
                os.system('clear')
                break

            try:
                #修改
                modify_names = input("请输入修改的用户名,end结束:")
                if modify_names == "end" :
                    os.system('clear')
                    break
                else :
                    self.card_imformation[self.names] = modify_names #修改用户名

                modify_ages = int(input("请输入修改的用户年龄(输入数字),end结束:"))
                if modify_ages == "end" :
                    os.system('clear')
                    break
                else :
                    self.card_imformation[self.ages] = modify_ages
                print("Error:值错误,只能输入数字!")
                modify_phone = input("请输入修改的用户电话号码,end结束:")
                if modify_address == "end" :
                    os.system('clear')
                    break
                else :
                    self.card_imformation[self.phone] = modify_phone

                modify_address = input("请输入修改的用户家庭住址,end结束:")
                if modify_address == "end" :
                    os.system('clear')
                    break
                else :
                    self.card_imformation[self.address] = modify_address
                    #names[names.index(modifycard)] = modify  #names.index()返回需要修改地方的索引值，将modify（修改内容）赋值给需要修改的地方，将原来的替换
                    print(self.lists)
            except ValueError:
                print("Error:值错误,只能输入数字!")


    # 查询用户名片内容
    def find_card(self): #输入索引值，查询其代表的用户内容
        """
        5. find_card --- 查询用户名片内容
        查询方式  --- 1.输入姓名查询 2.输入年龄查询 3.索引值查询 4.家庭住址查询(以end结束) 最后退出查询
        """
        while True :
            #os.system('clear')
            self.find_print()
            num = int(input("请输入查询方式:"))

            os.system('clear')
            if num == 1 : #如果是姓名查询
                name = input("请输入需要查询的用户姓名(输入字符串):")
                if name == "end" :
                    os.system('clear')
                    break
                else :
                    for i in self.lists :
                        if dict(i)['姓名'] == name : #如果找到查询的用户名字
                            print(dict(i)) #输出当为i时的字典
            elif num == 2 : #如果是年龄查询方式
                age = input("请输入要查询的年龄(输入数字):")
                if age == "end" :
                    os.system('clear')
                    break
                else :
                    for i in self.lists :
                        if dict(i)['年龄'] == age : #如果找到用户年龄
                            print(dict(i))
            elif num == 3 : #索引值查询
                index = int(input("请输入要查询的索引值(输入数字):"))
                if index == "end" :
                    os.system('clear')
                    break
                else :
                    try:
                        print(self.lists.index(index)) #输出索引值
                    except IndexError:
                        print("IndexError: 所查询的值不在索引范围内!")
            elif num == 4 : #家庭地址查询
                address = input("请输入要查询的年龄(输入数字):")
                if address == "end" :
                    os.system('clear')
                    break
                else :
                    for i in self.lists :
                        if dict(i)['家庭住址'] == address : #如果找到用户年龄
                            print(dict(i))
            elif num == 0 :
                break

    # 显示用户名片内容
    def display_card(self):
        """
        6. display_card --- 显示所有用户的名片内容
        """
        #os.system('clear')
        print("请输出名片内容: \n")
        print("{0:<10}\t{1:<10}\t{2:<10}\t{3:<10}" .format("姓名","年龄","电话号码","家庭住址",chr(12288)))
        #chr(12288)是python内置函数,12288是汉字unicode编码中的值,chr(12288)是将12288转换为中文空白字符
        #这里是采用chr(12288)表示中文空格
        for items in self.lists : #从列表中列出各个字典信息
            #for keys in i.items() : #迭代输出字典中的键值对
            #    print(keys)
            #    for key , value in i.items() :
            print("{0:<10}\t{1:<10}\t{2:<10}\t{3:<10}" .format(items["姓名"],items["年龄"],items["电话号码"],items["家庭住址"],chr(12288)))
        print("\n")

    def save_mysql(self):
        """
        7. save_mysql  ---  存储所有用户的信息到数据库
        数据库操作控制选项
        """
        save = Card_Mysql()
        while True :
            save.mysql_page() #打开数据库操作主界面
            num = int(input("请输入操作选项："))
            os.system('clear')
            if num == 1 :
                save.create_database()
            elif num == 2 :
                for items in self.lists :
                    name = items["姓名"]
                    age = items["年龄"]
                    phone = items["电话号码"]
                    address = items["家庭住址"]
                    save.save_data(name,age,phone,address)
            elif num == 0 :
                break


    # 退出名片管理系统
    def quit_card(self):
        """
        0. quit_card --- 退出名片管理系统
        """
        print("\n\n\n\n\n\n\n\n\n\n")
        print("="*50)
        print("\t\t谢谢您的使用!")
        print("="*50)
        print("\n\n\n\n\n\n\n\n\n\n")
        exit(0)

    def helpdocument():
        print(__doc__)
