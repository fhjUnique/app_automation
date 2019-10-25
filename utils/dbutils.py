# -*- coding: utf-8 -*-
from global_ import global_variable
import pymysql

# 打开数据库连接
db = pymysql.connect(host=global_variable.host,
                     port=int(global_variable.port),
                     user=global_variable.user,
                     password=global_variable.password,
                     db=global_variable.db,
                     charset=global_variable.charset,
                     cursorclass=pymysql.cursors.DictCursor)


def query(sql):
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行sql语句
    cursor.execute(sql)
    # 获取所有记录列表
    rows = cursor.fetchall()
    # 关闭数据库连接
    db.close()
    return rows


if __name__ == '__main__':
    r = query("SELECT * FROM batch_js_record")
    print(r[0])
