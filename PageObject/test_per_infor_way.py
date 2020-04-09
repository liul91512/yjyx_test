'''
  个人信息界面操作
'''
from selenium import webdriver
from YJYX_web_test.common.base import base
from YJYX_web_test.test_datas import locator
import time

class PerInfor:
    def __init__(self,driver):
        self.Base = base(driver)
        self.loc = locator.Locator()

    def per_infor_show(self):
        '''个人详细信息展示操作步骤'''
        self.Base.click(self.loc.loc_username)
        self.Base.click(self.loc.loc_person_infor)

    def per_infor_assert(self):
        '''个人详细信息断言：您的基本信息'''
        return self.Base.text(self.loc.loc_base_infor)

    def base_infor_change(self,name,phone):
        '''基本信息修改操作步骤'''
        self.Base.click(self.loc.loc_change_base_infor)
        time.sleep(1)
        self.Base.jquery_clear(self.loc.loc_realname)
        time.sleep(0.5)
        self.Base.jquery_val(self.loc.loc_realname,name)
        time.sleep(0.5)
        self.Base.jquery_clear(self.loc.loc_phone_num)
        time.sleep(0.5)
        self.Base.jquery_val(self.loc.loc_phone_num,phone)
        time.sleep(0.5)
        self.Base.jquery_click(self.loc.loc_quedin)

    def tishi_infor(self):
        '''提示信息文本获取,包括：用户信息修改成功、用户名不能为空、
           您没有修改信息、错误 : 原密码错误、请输入新密码！！、
           新密码和确认密码不同！、用户密码修改成功，点击确定，重新登录'''
        text = self.Base.text(self.loc.loc_tishi)
        self.Base.click(self.loc.loc_tishi_queding)
        return text

    def change_pwd(self,oldpwd,newpwd,qrpwd):
        '''登录密码修改步骤'''
        self.Base.click(self.loc.loc_change_login_pwd)
        time.sleep(1)
        self.Base.jquery_val(self.loc.loc_mypasswd,oldpwd)
        time.sleep(0.5)
        self.Base.jquery_val(self.loc.loc_change_pwd, newpwd)
        time.sleep(0.5)
        self.Base.jquery_val(self.loc.loc_queren_pwd, qrpwd)
        time.sleep(0.5)
        self.Base.jquery_click(self.loc.loc_queding)

if __name__ == '__main__':
    from YJYX_web_test.PageObject.test_login_way import Login
    driver = webdriver.Chrome()
    per = PerInfor(driver)
    driver.maximize_window()
    Login(driver).input_address()
    Login(driver).login("17774571997","lnbx-94963")
    per.per_infor_show()
    per.base_infor_change('12333','333')
    print(per.tishi_infor())



