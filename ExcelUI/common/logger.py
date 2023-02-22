# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/3/21 20:34
#  :TGW
"""
import logging


def test_log(file):
    #生成日志器
    logger = logging.getLogger()

    #设置日志等级
    logger.setLevel(logging.INFO)
    if not logger.handlers:

        #打印日志到控制台
        sh = logging.StreamHandler()
        logger.addHandler(sh)

        #打印日志到日志文件
        sf = logging.FileHandler(file,encoding='utf-8')
        logger.addHandler(sf)

        #设置日志格式
        fmt = '%(asctime)s %(filename)s %(funcName)s %(message)s'
        #生成格式器
        formatter = logging.Formatter(fmt)

        #把日志格式设置到控制台
        sh.setFormatter(formatter)

        #把日志格式设置到日志文件
        sf.setFormatter(formatter)

        return logger
