# -*- coding: utf-8 -*- 
"""          
# @Time : 2023/3/21 18:30
#  :TGW
"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from common.chrome_options import options

# 基于text值决定生成的driver对象是什么类型
def open_browser(text):
    if text == 'Chrome':
        driver = webdriver.Chrome(options=options())
    else:
        try:
            driver = getattr(webdriver, text)()
        except Exception as e:
            print("Exception Information:" + str(e))
            driver = webdriver.Chrome()
    return driver

class Keys:

    #初始化浏览器对象
    def __init__(self,text):
        self.driver = open_browser(text)
        self.driver.implicitly_wait(10)

    #打开网页
    def get_url(self,text):
        self.driver.get(text)

    #获取元素
    def locate(self,by,value):
        return self.driver.find_element(by,value)

    #点击
    def click(self,by,value):
        self.locate(by,value).click()

    #强制等待
    def sleep(self,text):
        sleep(int(text))

    #退出
    def quit(self):
        self.driver.quit()

    #输入内容
    def send_keys(self,by,value,text):
        self.locate(by,value).send_keys(text)

    #退出
    def quite(self):
        self.driver.quit()

    #切换句柄
    def swith_handle(self,text=1,close=True,):
        handles = self.driver.window_handles
        if close:
            self.driver.close()
        self.driver.switch_to.window(handles[text])

    #切换iframe框
    def swith_frame(self,value,by=None):
        if by:
            self.driver.switch_to.frame(value)
        self.driver.switch_to.frame(self.locate(by,value))

    #iframe切换默认内容
    def switch_default(self):
        self.driver.switch_to.default_content()

    #获取文本
    def get_text(self,name,value):
        return self.locate(name, value).text

    #获取页面标题
    def get_title(self):
        return self.driver.title

    #双击
    def double_click(self,by,value):
        ActionChains(self.driver).double_click(self.locate(by,value)).perform()

    #右击
    def context_click(self,by,value):
        ActionChains(self.driver).context_click(self.locate(by,value)).perform()

    #长按几秒松开
    def click_hold(self,by,value,text):
        ActionChains(self.driver).click_and_hold(self.locate(by,value)).perform()
        sleep(text)
        ActionChains(self.driver).release(self.locate(by,value)).perform()

    #鼠标悬停
    def move_to(self,by,value):
        ActionChains(self.driver).move_to_element(self.locate(by,value)).perform()

    #显示等待
    def driverwait(self,by,value):
        WebDriverWait(self.driver, 5, 0.5).until(lambda el: self.locate(by,value), message='显式等待查找失败')

    # 网页截图
    def screenshot(self,text):
     self.driver.save_screenshot(text)

    #js执行器
    def execute_script(self,by,value,text):
        self.driver.execute_script(text,self.locate(by,value))

    #滚动条
    def scrollto(self,x,y):
        js = f'window.scrollTo({x},{y})'
        self.driver.execute_script(js)

    # 定位元素，并在页面中心显示
    def scrollIntoView(self,by,name):
        js = 'arguments[0].scrollIntoView()'
        self.driver.execute_script(js,self.locate(by,name))

    # 获取元素属性的值
    def get_attribute(self,by,value,text):
        return self.locate(by,value).get_attribute(text)

    #断言结果是否相等
    def assert_text_equal(self,by,value,text):
        try:
            reality = self.locate(by,value).text
            assert text == reality
            return "True"
        except:
            return "False"

    #断言结果是否包含
    def assert_text_include(self,by,value,text):
        try:
            reality = self.locate(by,value).text
            assert text in reality
            return "True"
        except:
            return "False"

    #断言标题是否等于
    def assert_title_equal(self,text):
        try:
            reality = self.driver.title
            assert text in reality
            return "True"
        except:
            return "False"

    #退出
    def quit_browser(self):
        self.driver.quit()







