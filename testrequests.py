__author__ = 'tanteng'

import requests

def testrequests():

    url = 'http://www.x.com/index/pyrequests'

    params = {
        'x':'xxxx',
        'y':'yyyy'
    }

    re = requests.get(url,params)

    return re


if __name__ == '__main__':
    re = testrequests()
    print(re.text)

