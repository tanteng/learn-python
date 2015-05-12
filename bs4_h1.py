import urllib.request
from bs4 import BeautifulSoup
import sys

url = 'http://www.tantengvip.com'
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html)
h1s = soup.find_all('h1',class_='entry-title')

'''打印所有H1标题和链接'''
for h1 in h1s:
	#print(h1)
	print(h1.get_text())
	print(h1.a.attrs['href'])