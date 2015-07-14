import sys

# sys.argv接收参数，第一个参数是文件名，第二个参数开始是用户输入的参数，以空格隔开

def run1():
    print('I\'m action1')


def run2():
    print('I\'m action2')


if 2 > len(sys.argv):
    print('none')
else:
    action1 = sys.argv[1]
    action2 = sys.argv[2]

    if 'run1' == action1:
        run1()
    if 'run2' == action2:
        run2()
        
#用法：在命令行执行脚本，python sys_argv.py run1 run2
