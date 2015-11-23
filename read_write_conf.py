# encoding:utf-8

# !/usr/bin/env python

# -*- Python读写conf格式配置文件 -*-

__author__ = 'tanteng'


import configparser
import webbrowser

# 返回config对象
conf = configparser.ConfigParser()
conf.read('./conf/demo.conf', 'utf-8')

# 读取配置文件
def readConf():
    # 得到所有sections
    sections = conf.sections()
    print(sections)

    # 得到sec_a,sec_b的设置项
    options_sec_a = conf.options('sec_a')
    print(options_sec_a)

    options_sec_b = conf.options('sec_b')
    print(options_sec_b)

    # 得到sec_a,sec_b的设置键值对
    items_sec_a = conf.items('sec_a')
    print(items_sec_a)

    items_sec_b = conf.items('sec_b')
    print(items_sec_b)

    # 得到具体某个section某个option的值
    sec_a_key1 = conf.get('sec_a','a_key1')
    print(sec_a_key1)

readConf()

'''
readConf()运行结果：

['sec_a', 'sec_b']
['a_key1', 'a_key2']
['b_key1', 'b_key2', 'b_key3', 'b_key4']
[('a_key1', '20'), ('a_key2', '10')]
[('b_key1', '121'), ('b_key2', 'b_value2'), ('b_key3', '$r'), ('b_key4', '127.0.0.1')]
20
'''

# 写配置文件
def writeConf():
    # 更新某个section某个option的值
    conf.set('sec_a','a_key1','100') # 最后一个参数必须是string类型
    value = conf.get('sec_a','a_key1')
    print(value) # 打印结果看是否设置成功

    conf.add_section('new_section')
    conf.set('new_section','new_option_name','new_option_value')

    new_sections = conf.sections()

    # 检测是否新增section和新增设置项成功
    print(new_sections)
    print(conf.get('new_section','new_option_name'))


writeConf()

'''
writeConf()运行结果：

100
['sec_a', 'sec_b', 'website', 'new_section']
new_option_value
tantengdeMacBook-Pro:learn-python tanteng$
'''

# 更多Python3入门文章，读取网址配置跳转，现学现用

def jump():
    url = conf.get('website','url')
    webbrowser.open(url)

jump()
