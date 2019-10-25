# -*- coding: utf-8 -*-
import os
import time
import unittest
from global_ import global_cls
from utils import HTMLTestRunner, send_mail


def creatsuite():
    # 1---找到所有的test*py文件
    testunit = unittest.TestSuite()
    # 定义测试文件查找目录
    path = os.getcwd()
    test_dir = path + r'\test_case'
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(
        test_dir,
        pattern='test*.py',
        top_level_dir=None
    )
    # 2---discover方法筛选出来的用例，循环添加到测试套件中
    for test_case in discover:
        testunit.addTests(test_case)
    return testunit


# 自定义需要执行的用例
def custom():
    import test_case.test_a_login as a
    suite = unittest.TestSuite()
    suite.addTest(a.login_('test_001_success'))
    return suite


now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
filename = global_cls.report_path + now + '_result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='ys_test_report',
    description='test_case_description')
rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
log_path = global_cls.log_path
log_name = log_path + rq + '.log'

if __name__ == '__main__':
    # 执行全部用例
    alltestsuit = creatsuite()
    runner.run(alltestsuit)
    # 执行自定义用例
    # suite = custom()
    # runner.run(suite)
    fp.close()
    if global_cls.email_switch == 1:
        # 发送邮件方法
        send_mail.send_mail(filename, log_name)
