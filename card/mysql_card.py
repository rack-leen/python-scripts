#!/usr/bin/env python
# -*-coding=utf-8-*-
"""
  > File Nmae :mysql_card.py
  > Author    : rack
  > Function  :
  > Github    : https://github.com/rack-leen
  > Date      : Fri 03 Aug 2018 02:57:22 PM CST
"""

import MySQLdb  #导入数据库模块

class Card_Mysql:
    def __init__(self,username = 0,userpasswd = 0 ,name_database = 0 ,name_table = 0):
        """
        绑定实例
        """
        self.username = username
        self.userpasswd = userpasswd
        self.name_database = name_database
        self.name_table = name_table

    def mysql_page(self):
        """
        数据库操作主界面
        """
        print("\t\t数据库操作页")
        print("="*50)
        print("\t\t1. 创建数据库.")
        print("\t\t2. 保存数据.")
        print("\t\t0. 退出页面.")
        print("="*50)


    def create_database(self):
        """
        连接数据库，创建数据库与数据表
       """
        # 创建数据库
        print("开始创建数据库...")
        self.username = input("请输入你的mysql用户名：")
        self.userpasswd = input("请输入你的用户密码：")
        db = MySQLdb.connect(host="localhost",user=self.username,passwd=self.userpasswd) #打开数据库连接，参数分别为连接到本地连接，用户名，用户密码
        self.name_database = input("请输入你的数据库名：") #输入自己需要的数据库名
        cur_database = db.cursor() #使用curor创建一个游标对象
        #检查是否有同名数据库,有则删除，无则新建
        #cur_database.execute('drop database if exists '+ self.name_database)
        try:
            cur_database.execute('create database if not exists ' + self.name_database)
        except :
            print("Error:要创建的数据库已存在！")
        db.commit()#提交
        db.close()
        print("创建数据库成功!")

        #创建数据表
        print("开始创建数据表...")
        db = MySQLdb.connect(host="localhost",user=self.username,passwd=self.userpasswd,db=self.name_database)
        cur_table = db.cursor()
        self.name_table = input("请输入你需要创建的数据表：")#列字段

        #检查是否有数据表
        #cur_table.execute('drop table if exists '+ self.name_table) #如果有数据表则删除
        try:
            sql = "create table %s ( \
                name VARCHAR(50) PRIMARY KEY not null ,\
                age INT(10) , \
                phone INT(20),\
                address VARCHAR(50)) " %(self.name_table)  #创建card_table表
            cur_table.execute(sql) #如果没有则新建数据表
        except :
            print("Error:要创建的数据表已存在！")
        db.commit() #提交操作
        db.close() #关闭
        print("数据表创建成功！")

    def save_data(self,name,age,phone,address):
        """
        保存数据
        """

        print("保存数据...")
        db = MySQLdb.connect(host="localhost",user=self.username,passwd=self.userpasswd,db=self.name_database)
        cur_data = db.cursor()
        sql = "insert into %s(name,age,phone,address) values ('%s','%s','%s','%s')" %(self.name_table,name,age,phone,address)
        cur_data.execute(sql)
        db.commit()
        db.close()
        print("数据保存保存成功！")


