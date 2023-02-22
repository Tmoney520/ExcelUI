# -*- coding: utf-8 -*-
"""
# @Time : 2023/3/21 22:11
#  :TGW
"""
import os
from common.logger import test_log
from common.read_excel import read

if __name__ == '__main__':
    #创建logger对象
    log = test_log('./common/log.txt')
    #测试用例集合
    cases = list()
    #读取路径下的测试用例
    for path,dir,files in os.walk('./excel_data'):
        for file in files:
            #获取后缀名为.xlsx的用例文件
            if os.path.splitext(file)[1] == '.xlsx':
                cases.append(path + '/' + file)
    #执行每个用例文件的用例
    for case in cases:
        log.info(f'正在执行{case}文件的用例')
        read(log,case)