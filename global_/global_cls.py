# -*- coding: utf-8 -*-
from utils import rwExcel
import os

current_path = os.path.abspath(__file__)  # 获取当前文件路径
father_path = os.path.abspath(os.path.dirname(current_path))  # 获取当前文件的父目录
data_path = os.path.abspath(os.path.dirname(father_path)) + "\data\data.xls"  # 测试数据路径
testCase_path = os.path.abspath(os.path.dirname(father_path)) + "\data\\testCase.xls"  # 测试用例路径
log_path = os.path.abspath(os.path.dirname(father_path)) + "\Logs\\"  # 日志路径
report_path = os.path.abspath(os.path.dirname(father_path)) + "\\report\\"  # 报告路径
screen_path = os.path.abspath(os.path.dirname(father_path)) + "\erro_png\\"  # 错误截屏路径


#  存为字典
def up_dict(name, key_num):
    temp = {}
    for i in range(0, len(name)):
        key = []
        value = []
        key.append(name[i][key_num])
        value.append(name[i])
        temp.update(dict(zip(key, value)))
    return temp


# 读取配置表
config1 = rwExcel.readExcel(data_path, 'configure')
config = up_dict(config1, 1)
deviceName = config['deviceName'][0]  # 设备名称
platformName = config['platformName'][0]  # 设备平台
platformVersion = config['platformVersion'][0]  # 设备系统版本
autoAcceptAlerts = config['autoAcceptAlerts'][0]  # 是否接受弹窗的条款
noReset = config['noReset'][0]  # 是否不重复安装APP
appPackage = config['appPackage'][0]
appActivity = config['appActivity'][0]
log_switch = config['日志开关'][0]
email_switch = config['邮件开关'][0]
testCase_switch = config['结果写入用例开关'][0]

# 读取元素表
element1 = rwExcel.readExcel(data_path, 'element')
element = up_dict(element1, 3)


# 根据用例编号获取用例的行数
def get_row(bianhao):
    a = 0
    for i in testCase:
        if i[0] == bianhao:
            return a
        a = a + 1


# 根据title获取用例的列数
def get_col(title):
    a = 0
    for i in testCase[0]:
        if i == title:
            return a
        a = a + 1


# 读取测试用例
testCase = rwExcel.readExcel(testCase_path, 'Sheet1')
if testCase_switch == 1:
    # 初始化，把实际结果的值都置为空
    rwExcel.writeExcel_init(len(testCase), get_col('实际结果'))

# 读取数据库配置
# SQL_config = rwExcel.readExcel('MySQL_config')
# host = SQL_config[1][0]  # 数据库地址
# port = SQL_config[1][1]  # 端口号
# user = SQL_config[1][2]  # 用户名
# password = SQL_config[1][3]  # 密码
# db = SQL_config[1][4]  # 数据库名称
# charset = SQL_config[1][5]  # 编码格式

# 读取email配置
email_config = rwExcel.readExcel(data_path, 'email_config')
email_server = email_config[0][1]  # email_server
email_user = email_config[1][1]  # user
email_pass = email_config[2][1]  # password
email_receivers = []  # 接收邮件人
for i in range(1, len(email_config[3])):
    email_receivers.append(email_config[3][i])
