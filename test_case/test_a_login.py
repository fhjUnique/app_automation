# -*- coding: utf-8 -*-

from global_ import global_cls
from utils.log import Logger
from utils import Assertion
from test_case.public import login
import unittest, time
from utils.WebTools import WebTools

my_logger = Logger(logger='Login').getlog()
web = WebTools()
web_switch = True


# 登录模块
class login_(unittest.TestCase):
    def setUp(self):
        global web_switch
        if web_switch == 1:
            web_switch = False
            web.start_app()  # 启动手机APP
        my_logger.info('**********************登录模块**************************')
        web.wait_implicit(20)

    # 用户名正确，密码错误
    def test_000_pwd_error(self):
        my_logger.info('--------用户名正确，密码错误---------')
        login.login(web, 'df.rep@shgvp.stg', 'Welcome')
        time.sleep(1)
        text = web.get_text(global_cls.element['login_error'], '获取密码错误提示')
        Assertion.verifyEquals(web, text, '密码错误!', '验证用户名正确，密码错误是否可以登录')
        # Assertion.verifyHaveElement(web, global_cls.element['登录成功'], 'testtesttest')
        Assertion.assertEnd('ystx-001')

    # 用户名密码都正确
    # def test_001_success(self):
    #     global web_switch
    #     web_switch = True
    #     my_logger.info('--------用户名密码都正确---------')
    #     login.login(web, 'df.rep@shgvp.stg', 'Welcome123')
    #     time.sleep(1)
    #     Assertion.verifyHaveElement(web, global_cls.element['菜单栏'], '验证用户名密码都正确是否可以登录成功')
    #     Assertion.assertEnd('ystx-002')

    def tearDown(self):
        if web_switch == 1:
            my_logger.info('退出App')
            web.stop_app()


if __name__ == '__main__':
    unittest.main()
