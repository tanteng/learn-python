# encoding:utf-8

# !/usr/bin/env python

# -*- Python3命令行 -*-

import optparse
import sys
import webbrowser


def process_command_line(argv):
    """
    Return a 2-tuple: (settings object, args list).
    `argv` is a list of arguments, or `None` for ``sys.argv[1:]``.
    """
    if argv is None:
        argv = sys.argv[1:]
    # initialize the parser object:
    parser = optparse.OptionParser(
        formatter=optparse.TitledHelpFormatter(width=78),
        add_help_option=None)
    # define options here:
    parser.add_option(      # customized description; put --help last
        '-h', '--help', action='help',
        help='Show this help message and exit.')
    parser.add_option(
        '-u', '--url', action='store', dest = 'link',
        help='Open a link.')
    settings, args = parser.parse_args(argv)
    # check number of arguments, verify values, etc.:
    if args:
        parser.error('program takes no command-line arguments; '
                     '"%s" ignored.' % (args,))
    # further process settings & args if necessary
    return settings, args

def main(argv=None):
    settings, args = process_command_line(argv)
    print(settings)
    # application code here, like:
    run(settings, args)
    return 0        # success

def run(settings, args):
    if settings.link:
        webbrowser.open(settings.link, 1)


if __name__ == '__main__':
    status = main()
    sys.exit(status)

"""
命令行功能：

python sys_argv.py -h
显示帮助信息

python sys_argv.py -u www.163.com
用默认浏览器打开你输入的网址
"""