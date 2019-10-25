# -*- coding: utf-8 -*-
from xlutils.copy import copy
import xlrd, os
from xlwt import *


# 读取Excel表
def readExcel(data_path, sheetname):
    wb = xlrd.open_workbook(data_path)  # 打开Excel
    sh = wb.sheet_by_name(sheetname)  # 读取哪个表
    row = sh.nrows  # 共有多少行
    col = sh.ncols  # 共有多少列
    ss = []
    for i in range(0, row):
        s = sh.row_values(i)
        ss.append(s)
    return ss  # 返回类型为list[[],[],[]]，一行为一个小集合


current_path = os.path.abspath(__file__)  # 获取当前文件路径
father_path = os.path.abspath(os.path.dirname(current_path))  # 获取当前文件的父目录
testCase_path = os.path.abspath(os.path.dirname(father_path)) + "\data\\testCase.xls"  # 测试用例路径


# 写入Excel表
def writeExcel(name, list_):  # 写入为list[[row,col,message],[row,col,message],[row,col,message]]格式
    rb = xlrd.open_workbook(testCase_path, formatting_info=True)  # 打开已有的Excel，formatting_info=True，得以保存之前数据的格式
    wbk = copy(rb)  # copy去从打开的xlrd的Book变量中，拷贝出一份，成为新的xlwt的Workbook变量
    sheet1 = wbk.get_sheet(name)

    style = XFStyle()  # 创建一个样式对象，初始化样式
    pattern = Pattern()
    pattern.pattern = Pattern.SOLID_PATTERN  # 设置其模式为实型
    pattern.pattern_fore_colour = 50   # 设置单元格背景颜色 绿色
    style.pattern = pattern
    alignment = Alignment()  # 设置字体在单元格的位置
    alignment.horz = Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = Alignment.VERT_CENTER  # 竖直方向
    style.alignment = alignment
    font = Font()  # 字体基本设置
    font.name = u'微软雅黑'
    font.colour_index = 1  # 白色
    font.height = 220  # 字体大小，220就是11号字体，大概就是11*20得来的吧
    style.font = font
    borders = Borders()
    borders.bottom = 1
    style.borders = borders

    for i in range(0, len(list_)):
        if list_[i][2] == 'fail':
            pattern.pattern_fore_colour = 10  # 设置单元格背景颜色 红色
        style.pattern = pattern
        sheet1.write(list_[i][0], list_[i][1], list_[i][2], style)
    wbk.save(testCase_path)  # 保存Excel表


def writeExcel_init(len, col):
    for x in range(len - 1):
        writeExcel('Sheet1', [[x + 1, col, '']])

# 用法示例
# if __name__ == '__main__':
# list_ = [[5, 0, '啦啦啦5'], [5, 1, '啦啦啦55']]
#     print(list_)
#     writeExcel('MySQL_config', list_)
