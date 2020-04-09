'''
   查找元素方法封装
'''
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from YJYX_web_test.common import log_test
# from selenium.webdriver.support import expected_conditions as EC

class base():
    def __init__(self,driver:webdriver.Chrome):
        self.driver = driver
        self.timeout = 15
        self.poll = 0.5

    def findElement(self,locator,name="截图"):
        '''
        查找单一元素，用显示等待方式
        '''
        try:
            element = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x : x.find_element(*locator))
            return element
        except:
            log_test.get_logger("元素定位失败")
            self.save_screenshot(name)
            raise

    def findElements(self,locator,name="截图"):
        '''
        查找多个元素，用显示等待方式
        '''
        try:
            elements = WebDriverWait(self.driver,self.timeout,self.poll).until(lambda x : x.find_elements(*locator))
            return elements
        except:
            log_test.get_logger("元素定位失败")
            self.save_screenshot(name)
            raise

    def save_screenshot(self,name):
        '''
        截图操作
        :param name: 截图文件名
        '''
        #截图存放路径
        file_name = r"F:\Pyth\YJYX_web_test\result\screenshots"+"\{}.jpg".format(name)
        self.driver.save_screenshot(file_name)
        log_test.get_logger("截图成功，文件路径为：{}".format(file_name))

    def click(self,locator):
        '''
        click点击
        '''
        ele = self.findElement(locator)
        ele.click()

    def sendKeys(self,locator,text):
        '''
        sendkeys输入
        '''
        ele = self.findElement(locator)
        ele.send_keys(text)

    def clear(self,locator):
        '''
        clear清空
        '''
        ele = self.findElement(locator)
        ele.clear()

    def text(self,locator):
        '''
        text获取文本
        '''
        ele = self.findElement(locator)
        return ele.text

    def is_element_exist(self,locator):
        '''
        单数定位时，判断元素是否存在
        '''
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def is_elements_exist(self,locator):
        '''
        复数定位时，判断元素是否存在
        '''
        try:
            ele = self.findElements(locator)
            count = len(ele) # 计算定位到的元素个数
            if count == 0:
                return False
            else:
                return "定位到的元素个数为：%s" % count
        except:
            return False

    def is_displayed_exist(self,locator):
        '''
        判断元素是否在当前视窗显示，即不是隐藏元素
        '''
        ele = self.findElement(locator)
        return ele.is_displayed()

    def is_selected_exist(self,locator):
        '''
        判断select下拉框是否被选中
        '''
        ele = self.findElement(locator)
        return ele.is_selected()

    def is_radio(self,locator):
        '''
        判断单选框是否被选中
        '''
        ele = self.findElement(locator)
        return ele.is_selected()

    def is_checkbox(self,locator):
        '''
        判断复选框是否被选中
        '''
        eles = self.findElements(locator)
        count = len(eles)
        if count == 0:
            return False
        else:
            return "选中的个数为：{}".format(count)

    def is_all_checkbox(self,locator):
        '''
        全部选中复选框
        '''
        eles = self.findElements(locator)
        for i in eles:
            if not i.is_selected():
                i.click()

    def is_enabled(self,locator):
        '''
        判断元素是否可以被操作（点击、输入文本等）
        '''
        ele = self.findElement(locator)
        return ele.is_enabled()

    def title_is(self,text):
        '''
        判断title
        '''
        try:
            title = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.title_is(text))
            return title
        except:
            return False

    def title_contains(self,text):
        '''
        判断预期title是否包含于实际title
        '''
        try:
            title = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.title_contains(text))
            return title
        except:
            return False

    def text_in_element(self,locator,text):
        '''
        判断元素文本是否相等
        '''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element(locator,text))
            return result
        except:
            return False

    def text_in_element_value(self,locator,text):
        '''
        判断元素的value属性是否相等
        '''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.text_to_be_present_in_element_value(locator,text))
            return result
        except:
            return False

    def alert_is(self):
        '''
        判断是否有alert弹框
        '''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.poll).until(EC.alert_is_present())
            return result
        except:
            return False

    def js_scroll_end(self):
        '''
        js操作浏览器滚动到底部
        '''
        js = "window.scrollTo(0,document.body.scrollHeight);"
        self.driver.execute_script(js)

    def js_scroll_top(self):
        '''
        js操作浏览器滚动到顶部
        '''
        js = "window.scrollTo(0,0);"
        self.driver.execute_script(js)

    def js_focus(self,locator):
        '''
        滚动到元素出现位置(聚焦元素)
        '''
        target = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def js_div_scroll_top_by_id(self,Id,height):
        '''
        js通过id控制纵向内嵌div滚动条
        '''
        js = "document.getElementById('{}').scrollTop = {};".format(Id,height)
        self.driver.execute_script(js)

    def js_div_scroll_left_by_id(self,Id,weight):
        '''
        js通过id控制横向内嵌div滚动条
        '''
        js = "document.getElementById('{}').scrollTop = {};".format(Id,weight)
        self.driver.execute_script(js)

    def js_readonly_by_id(self,Id):
        '''
        js通过id去除日历控件readonly属性
        '''
        js = "document.getElementById('%s').removeAttribute('readonly');" % Id
        self.driver.execute_script(js)

    def js_readonly_by_name(self,name):
        '''
        js通过name去除日历控件readonly属性
        '''
        js = "document.getElementsByName('%s')[0].removeAttribute('readonly');" % name
        self.driver.execute_script(js)

    def js_readonly_by_tagname(self,tagname):
        '''
        js通过标签去除日历控件readonly属性
        '''
        js = "document.getElementsByTagName('%s')[0].removeAttribute('readonly');" % tagname
        self.driver.execute_script(js)

    def js_readonly_by_class(self,classname):
        '''
        js通过class去除日历控件readonly属性
        '''
        js = "document.getElementsByClassName('%s')[0].removeAttribute('readonly');" % classname
        self.driver.execute_script(js)

    def js_iframe_by_id(self,Id,text):
        '''
        js通过id处理有iframe的富文本
        '''
        js = "document.getElementById('{}').contentWindow.document.body.innerHTML='{}';".format(Id,text)
        self.driver.execute_script(js)

    def js_iframe_by_name(self,name,text):
        '''
        js通过name处理有iframe的富文本
        '''
        js = "document.getElementsByName('{}')[0].contentWindow.document.body.innerHTML='{}';".format(name,text)
        self.driver.execute_script(js)

    def js_iframe_by_tagname(self,tagname,text):
        '''
        js通过标签处理有iframe的富文本
        '''
        js = "document.getElementsByTagName('{}')[0].contentWindow.document.body.innerHTML='{}';".format(tagname,text)
        self.driver.execute_script(js)

    def js_iframe_by_class(self,classname,text):
        '''
        js通过class处理有iframe的富文本
        '''
        js = "document.getElementsByClassName('{}')[0].contentWindow.document.body.innerHTML='{}';".format(classname,text)
        self.driver.execute_script(js)

    def js_value_by_id(self,Id,value):
        '''
        js通过id修改value属性
        '''
        self.js_readonly_by_id(Id)
        js = "document.getElementById('{}').value = '{}';".format(Id,value)
        self.driver.execute_script(js)

    def js_click_by_id(self,Id):
        '''
        js通过id解决click失效问题
        '''
        js = "document.getElementById('%s').click();" % Id
        self.driver.execute_script(js)

    def js_click_by_name(self,name):
        '''
        js通过name解决click失效问题
        '''
        js = "document.getElementsByName('%s')[0].click();" % name
        self.driver.execute_script(js)

    def js_click_by_tagname(self,tagname):
        '''
        js通过标签解决click失效问题
        '''
        js = "document.getElementsByTagName('%s')[0].click();" % tagname
        self.driver.execute_script(js)

    def js_click_by_class(self,classname):
        '''
        js通过class解决click失效问题
        '''
        js = "document.getElementsByClassName('%s')[0].click();" % classname
        self.driver.execute_script(js)

    def file_upload_input(self,locator,path):
        '''
        仅用于文件上传按钮是input标签
        '''
        self.findElement(locator).send_keys(path)

    def file_upload(self,uploadpath,title,filepath):
        '''
        文件上传，任何类型的上传都可以
        uploadpath: 执行上传功能的.exe文件路径
        title: 上传窗口title
        filepath: 需上传文件路径
        '''
        os.system("{} {} {}".format(uploadpath,title,filepath))

    def move_mouse_click(self,locator1,locator2):
        '''
        鼠标移动到下拉框，出现下拉框后选择
        '''
        mouse = self.findElement(locator1)
        ActionChains(self.driver).move_to_element(mouse).perform()
        self.click(locator2)

    def jquery_val(self,css_loc,value):
        '''
        jquery方式输入文本内容
        :param css_loc: css定位
        :param value: 文本内容
        '''
        jq = '''$("{0}").val("{1}");'''.format(css_loc,value)
        self.driver.execute_script(jq)

    def jquery_click(self,css_loc):
        '''
        jquery方式点击
        :param css_loc: css定位
        '''
        jq = '''$("{0}").click();'''.format(css_loc)
        self.driver.execute_script(jq)

    def jquery_clear(self,css_loc):
        '''
        清空文本
        '''
        jq = '''$("{0}").val("");'''.format(css_loc)
        self.driver.execute_script(jq)

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    a = base(driver)
    a.jquery_val("input[id='kw']",'百度')
    a.js_click_by_id("su")
    # a.file_upload("D:\\upload.exe","打开","D:\\123.txt")
    # driver = webdriver.Chrome()
    # driver.get("https://www.12306.cn/index/")
    # time.sleep(2)
    # a = base(driver)
    # a.js_value_by_id('train_date','2020-02-05')
    # driver.get("https://www.baidu.com")
    # a = base(driver)
    # a.sendKeys(("id","kw"),"中国")
    # a.js_click_by_id('su')
    # driver.get("https://pan.baidu.com/")
    # a = base(driver)
    # a.click(("id","TANGRAM__PSP_4__footerULoginBtn"))
    # a.sendKeys(("id","TANGRAM__PSP_4__userName"),"14760701301")
    # a.sendKeys(("id","TANGRAM__PSP_4__password"),"lnbx-94963")
    # a.click(("id","TANGRAM__PSP_4__submit"))

#     from selenium.webdriver.support import expected_conditions as EC
#     driver = webdriver.Chrome()
#     driver.get("https://www.baidu.com")
#     result = FindElement(driver)
#     a = result.text_in_element_value(("id","su"),"百度一下")
#     print(a)

    # from selenium.webdriver.common.action_chains import ActionChains
    # driver = webdriver.Chrome()
    # driver.get("file:///F:/form%E8%A1%A8%E5%8D%95.html")
    # a = FindElement(driver)
    # a.is_all_checkbox(("css selector","[type='checkbox']"))

    # mouse = baidu.findElement(("link text","设置"))
    # ActionChains(driver).move_to_element(mouse).perform()
    # baidu.click(("link text","搜索设置"))
    # # print(baidu.is_radio(("id","s1_1")))
    # baidu.click(("id","nr"))
    # baidu.click(("xpath","//*[@id='nr']/option[3]"))
    # a = baidu.is_selected_exist(("xpath","//*[@id='nr']/option[3]"))
    # print(a)
    # baidu.click(("link text","保存设置"))
    # driver.switch_to.alert.accept()
#     zentao = FindElement(driver)
#     loct1 = ("id","userName")
#     loct2 = ("id","password")
#     loct3 = ("id","but_login")
#
#     zentao.sendKeys(loct1,"testxt")
#     time.sleep(1)
#     zentao.sendKeys(loct2,"songqintest")
#     time.sleep(1)
#     zentao.click(loct3)

















