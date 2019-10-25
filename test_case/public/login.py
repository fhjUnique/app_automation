# -*- coding: utf-8 -*-
from utils.log import Logger
from global_ import global_cls
import time

my_logger = Logger(logger='login').getlog()


def login(web, username, password):
    web.clear(global_cls.element['username'])
    web.input(global_cls.element['username'], username, '输入用户名')
    web.clear(global_cls.element['password'])
    web.input(global_cls.element['password'], password, '输入密码')
    time.sleep(2)
    web.click(global_cls.element['login_bt'], '点击登录')
