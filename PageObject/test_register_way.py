'''
   注册页面操作
'''
from selenium import webdriver
from YJYX_web_test.common.base import base
from YJYX_web_test.test_datas import locator

class Register:
    def __init__(self,driver):
        self.Base = base(driver)
        self.loc = locator.Locator()

    def register(self,name='',
                 phone='',
                 yanzm='',
                 passwd='',
                 qpasswd=''):
        '''注册操作'''
        self.Base.sendKeys(self.loc.locator_teacher_name,name)
        self.Base.sendKeys(self.loc.locator_input_phone,phone)
        self.Base.sendKeys(self.loc.locator_yanzhengma,yanzm)
        self.Base.sendKeys(self.loc.locator_passwd,passwd)
        self.Base.sendKeys(self.loc.locator_queren_passwd,qpasswd)
        self.Base.click(self.loc.locator_register_button)

    def register_success(self):
        '''注册成功获取元素'''
        pass

    def not_input_phone(self):
        '''不输入手机号注册提示信息获取'''
        return self.Base.text(self.loc.loc_not_input_phone)

    def input_error_phone(self):
        '''输入错误格式手机号注册提示信息获取'''
        return self.Base.text(self.loc.loc_input_error_phone)

    def not_input_yanzhengma(self):
        '''不输入验证码注册提示信息获取'''
        return self.Base.text(self.loc.loc_not_input_yanzhengma)

    def input_error_yanzhengma(self):
        '''输入错误验证码注册提示信息获取'''
        return self.Base.text(self.loc.loc_input_error_yanzhengma)

    def not_input_pwd(self):
        '''不输入密码及输入少于6位密码注册提示信息获取'''
        return self.Base.text(self.loc.loc_not_input_passwd)

    def not_same_pwd(self):
        '''两次密码输入不一致注册提示信息获取'''
        return self.Base.text(self.loc.loc_not_same_passwd)

if __name__ == '__main__':
    from YJYX_web_test.PageObject import test_login_way
    driver = webdriver.Chrome()
    driver.get("http://www.zgyjyx.com/teacher/login/login.html")
    lo = test_login_way.Login(driver)
    lo.register()
    yj = Register(driver)
    yj.register()
    print(yj.not_input_phone())