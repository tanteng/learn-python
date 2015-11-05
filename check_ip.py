#!/usr/bin/python
#coding:utf-8

import urllib.request
import re
import sys

def ISIP(s):
    return len([i for i in s.split('.') if (0<= int(i)<= 255)])== 4

def URL(ip):
    uip = urllib.request.urlopen('http://wap.ip138.com/ip.asp?ip='+ip)
    fip = uip.read()
    rip = re.compile("<br/><b>查询结果：(.*)</b><br/>")
    result = rip.findall(fip)
    print("%s\t %s" % (ip, result[0]))


def DO(domain):
    url = urllib.request.urlopen('http://wap.ip138.com/ip.asp?ip='+domain)
    f = url.read().decode('utf-8')
    r = re.compile('<br/><b>查询结果：(.*)</b><br/>')
    result = r.findall(f)
    #print type(result)
    for i in result:
        print("%s %s %s" % (domain, i[0], i[1]))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("请输入IP地址或者域名 (例如:192.168.1.1 / www.baidu.com)")
        sys.exit()
    INPUT=sys.argv[1]
    if not re.findall('(\d{1,3}\.){3}\d{1,3}',INPUT):
        if re.findall('(\w+\.)?(\w+)(\.\D+){1,2}',INPUT) :
            DOMAIN=INPUT
            DO(DOMAIN)
        else:
            print("输入的IP地址和域名格式不对！")
    else:
        if ISIP(INPUT) :
            IPADDRESS=INPUT
            URL(IPADDRESS)
        else:
            print("IP 地址不合法，请重新输入！")
