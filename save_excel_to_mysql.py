# -*- coding:utf-8 -*-
import xlrd
import MySQLdb
import os
import logging
import shutil
import sys


def main(path):
    """
    打开目录遍历excel文件并存储到mysql
    """
    files = os.listdir(path)
    for file in files:
        save_file(path + '/' + file, file)
        print(file)


def save_file(file, filename):
    """
    打开excel文件
    """
    try:
        book = xlrd.open_workbook(file)
        sheet = book.sheet_by_index(0)
    except Exception as e:
        logging.info('错误：{0} 文件：{1}'.format(e, file))
        shutil.copy2(file, './error' + filename)
        return False
    row_nums = sheet.nrows
    col_nums = sheet.ncols

    page = False  # 是否分几次插入

    data = []
    if row_nums < 2:
        return False
    if col_nums not in [23, 25]:  # 两种excel格式，一个23列，一个25列
        return False

    for rownumber in range(1, row_nums):
        if page is True:
            data = []
        values = sheet.row_values(rownumber)
        values.insert(0, 0)
        if values[1] == '':
            return False

        # 不同形式表格差异处理
        if col_nums == 23:
            values.insert(7, '')
            values.insert(8, '')

        if values[20] == '':
            values[20] == '0000-00-00 00:00:00'
        if values[21] == '':
            values[21] = '0000-00-00 00:00:00'

        data.append(tuple(values))
        totals = len(data)
        page = False
        if totals >= 2000:
            insert(data)
            page = True
            del data

    insert(data)
    return True


def insert(data):
    """
    将excel表格所有数据一次插入到mysql中
    """
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="fahuo", use_unicode=True, charset="utf8")
    c = db.cursor()

    try:
        c.executemany(
            """INSERT INTO `order` VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            data)
        db.commit()
    except Exception as e:
        logging.info(e)
        db.close()
        return False
    return True


if __name__ == "__main__":
    logging.basicConfig(filename='./log.txt', level=logging.DEBUG)
    path = './excel'
    main(path)
