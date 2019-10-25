# -*- coding: utf-8 -*-
from utils.log import Logger
from global_ import global_cls
from utils.rwExcel import writeExcel
import time

mylogger = Logger(logger='Assertion').getlog()
errors = []


# 实际值与预期值的对比 如果实际值与预期值相等则pass，否则fail
def verifyEquals(web_tools, actual, expected, title):
    mylogger.info(title)
    try:
        assert actual == expected
        mylogger.info('pass!!!')
    except Exception as e:
        errors.append(e)
        mylogger.error('fail:  ' + " '" + actual + "'  !=  '" + expected)
        web_tools.screen_shot(title)


# 实际值与预期值的对比 如果实际值与预期值不等则pass，否则fail
def verifyNotEquals(web_tools, actual, expected, title):
    mylogger.info(title)
    try:
        assert actual != expected
        mylogger.info('pass!!!')
    except Exception as e:
        errors.append(e)
        mylogger.error('fail:  ' + " '" + actual + "'  ==  '" + expected)
        web_tools.screen_shot(title)


# 值是否包含a  如果包含则pass，否则fail
def verifyInContain(web_tools, contain, a, title):
    mylogger.info(title)
    try:
        assert a in contain
        mylogger.info('pass!!!')
    except Exception as e:
        errors.append(e)
        mylogger.error('fail:  ' + " '" + a + "'  not in  '" + contain)
        web_tools.screen_shot(title)


# 判断元素是否存在
def verifyHaveElement(web_tools, ele, title):
    mylogger.info(title)
    try:
        web_tools.find_have_element(ele)
        mylogger.info('pass!!!')
    except Exception as e:
        errors.append(e)
        mylogger.error('fail')
        web_tools.screen_shot(title)


# 判断元素是否不存在
def verifyNoneElement(web_tools, ele, title):
    mylogger.info(title)
    try:
        time.sleep(1)
        web_tools.find_have_element(ele)
        mylogger.error('fail:  ' + title)
        web_tools.screen_shot(title)
        errors.append(1)
    except Exception as e:
        mylogger.info('pass!!!')


# 判断用例是否含有验证失败的断言，如果有此方法会抛出异常
# 如果没有不会抛出异常，会认为用例成功
# 结果写入用例Excel
def assertEnd(bianhao='null'):
    row = global_cls.get_row(bianhao)
    col = global_cls.get_col('实际结果')
    a = len(errors)
    del errors[:]
    if global_cls.testCase_switch == 1 and bianhao != 'null':
        if a == 0:
            writeExcel('Sheet1', [[row, col, '通过']])
        else:
            writeExcel('Sheet1', [[row, col, '未通过']])
    assert a == 0, '本条用例执行失败！'


# 统计失败断言的数量
def assert_errors():
    a = len(errors)
    return a
