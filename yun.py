#coding=utf-8
import urllib.request
import re
import os
import sys
 
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
 
 
def getVideo(html):
    reg = r'hurl=(.+?\.jpg)'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    return imglist
 
for num in range(28000,1000000):
    print (num)
    html = getHtml("http://music.163.com/mv?id=%s"%num)
    html = html.decode('utf-8')
    parsed = getVideo(html)
    print(parsed)
    if len(parsed)==0:
        continue
    vedioUrls = parsed[0].split("&")
 
    artist = vedioUrls[4].split("=")[1].strip()
    song = vedioUrls[3].split("=")[1].strip()
    if  len(vedioUrls[0])==0:
        continue
    filename = '%s/%s.mp4' %(artist,song)
    if "/" in song:
        continue
     
    if os.path.exists(filename):
        print ('the MV file exists.%s'%num)
    else:
        print ('the MV is downloding.%s'%num)
        if  os.path.exists(artist):
            print ("")
        else:
            os.makedirs(artist)
        urllib.request.urlretrieve(vedioUrls[0],filename)