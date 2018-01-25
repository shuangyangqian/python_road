#! /usr/bin/env python
# -*- coding: utf-8 -*-

# author
# email: shuangyang.qian@easystack.cn
# irc: qsyqian

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>


Options:
    -h,--help      显示帮助菜单
    -g             高铁
    -d             动车
    -t             特快
    -k             快速
    -z             直达


Example:
    tickets 郑州 北京 2018-01-01
    tickets -dg 北京 郑州 2018-01-02
"""

from docopt import docopt


def cli():
    """
    command-line interface
    :return:
    """
    arguments = docopt(__doc__)
    print arguments


if __name__ == "__main__":
    cli()
