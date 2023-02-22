# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/3/21 20:19
#  :TGW
"""
from selenium import webdriver


def options():
    # chrome浏览器的配置项，可以通过修改默认参数，改变默认启动的浏览器的形态
    options = webdriver.ChromeOptions()

    # 页面加载策略
    options.page_load_strategy = 'eager'

    # 将浏览器默认设置为最大窗体
    options.add_argument('start-maximized')

    # 设置默认窗体的启动大小
    # options.add_argument('window-size=400,2000')

    # 无头模式：虽然看不到，但是一切照旧，在一些特定场景下会失败
    # options.add_argument('--headless')

    # 去掉默认的提示自动化信息：没啥用，一般没有什么影响。警告条可能会导致页面内容的遮挡或者挤压，影响自动化测试
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

    # 去掉控制台多余信息
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # 读取本地缓存，实现一个有缓存的浏览器，这个指令执行前必须关闭所有本地的chrome浏览器
    # 先chrome：//version找到个人资料路径，复制到Default前
    # options.add_argument(r'--user-data-dir=路径')

    # 去掉账号密码弹窗，一般是询问是否要保存账号密码
    prefs = {}
    prefs["credentials_enable_service"] = False
    prefs['profile.password_manager_enable'] = False
    options.add_experimental_option("prefs", prefs)

    # 指定窗口打开在哪个位置
    # options.add_argument('window-position=2200,500')

    # 隐身模式（不出现浏览器）
    # options.add_argument('incognito')

    return options