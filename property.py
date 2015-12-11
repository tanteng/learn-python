__author__ = 'tanteng'

class Ver(object):
    def __init__(self,version):
        self.version = version

    @property
    def version_no(self):
        return self.version


ver = Ver('2.0')
print(ver.version_no)