# coding=utf-8
from decimal import *
import time


# 四舍五入
def rounding(string, state):
    a = '0.'
    b = '0'
    c = a + b * state
    num = Decimal(string).quantize(Decimal(c))
    return str(num)

