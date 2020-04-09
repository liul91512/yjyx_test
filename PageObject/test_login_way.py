'''
   YJYX登录页面操作
'''
from selenium import webdriver
from YJYX_web_test.common.base import base
from YJYX_web_test.test_datas import locator

class Login:
    def __init__(self,driver):
        '''初始化'''
        self.driver = driver
        self.Base = base(driver)
        self.loc = locator.Locator()

    def input_address(self):
        '''输入地址'''
        self.driver.get(self.loc.locator_address)

    def login(self,user='',pwd=''):
        '''登录操作'''
        self.Base.sendKeys(self.loc.locator_user,user)
        self.Base.sendKeys(self.loc.locator_pwd,pwd)
        self.Base.click(self.loc.locator_login)

    def login_success(self):
        '''登录成功获取元素'''
        return self.Base.text(self.loc.locator_success)

    def login_fail(self):
        '''登录失败获取元素'''
        return self.Base.text(self.loc.locator_fail)

    def remember_me(self):
        '''记住我'''
        self.Base.click(self.loc.locator_remember_me)

    def register(self):
        '''注册入口'''
        self.Base.click(self.loc.locator_register)

    def forget_passwd(self):
        '''忘记密码入口'''
        self.Base.click(self.loc.locator_forget_passwd)

    def enter_register_success(self):
        '''进入注册页面成功获取元素'''
        return self.Base.text(self.loc.loc_enter_register_succeess)

    def enter_forget_success(self):
        '''进入忘记密码页面成功'获取元素'''
        return self.Base.text(self.loc.loc_enter_forget_success)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    Login(driver).input_address()
