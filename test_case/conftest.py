'''
   YJYX测试准备与清理
'''
import pytest
from selenium import webdriver
from YJYX_web_test.PageObject.test_login_way import Login
from YJYX_web_test.PageObject.test_register_way import Register
from YJYX_web_test.common.base import base
from YJYX_web_test.PageObject.test_per_infor_way import PerInfor
from YJYX_web_test.test_datas.login_datas import PhoneDatas as PD
import time

'''
登录测试准备与清理
'''
driver = None
@pytest.fixture(scope='class')
def set_updown_class_login():
    global driver
    #前置操作
    driver = webdriver.Chrome()
    login = Login(driver)
    login.input_address()
    yield (driver,login)
    #后置操作
    driver.quit()

@pytest.fixture
def set_updown_login():
    global driver
    #前置操作
    if base(driver).alert_is():
        driver.switch_to.alert.accept()
    driver.delete_all_cookies()
    driver.refresh()
    yield
    #后置操作

'''
注册测试准备与清理
'''
@pytest.fixture(scope="class")
def set_updown_class_register():
    global driver
    #前置操作
    driver = webdriver.Chrome()
    login = Login(driver)
    register = Register(driver)
    login.input_address()
    login.register()
    yield (driver,register)
    #后置操作
    driver.quit()

@pytest.fixture
def set_updown_register():
    global driver
    #前置操作
    driver.refresh()
    yield
    #后置操作

'''
个人信息界面测试准备与清理
'''
@pytest.fixture(scope="class")
def set_updown_class_perinfor():
    global driver,per
    #前置操作
    driver = webdriver.Chrome()
    login = Login(driver)
    per = PerInfor(driver)
    driver.maximize_window()
    login.input_address()
    login.login(PD.normal_datas["username"],PD.normal_datas["password"])
    yield (driver,per)
    #后置操作
    driver.quit()

@pytest.fixture
def set_updown_perinfor():
    global driver,per
    #前置操作
    per.per_infor_show()
    yield
    #后置操作
    driver.refresh()
