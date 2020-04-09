'''
   YJYX定位信息
'''
from selenium.webdriver.common.by import By

class Locator:
    '''登录界面定位'''
    locator_address = "http://njqa.zgyjyx.net/teacher/login/login.html" #登录地址
    locator_user = (By.ID,'username') #用户名框定位
    locator_pwd = (By.ID,'password')  #密码框定位
    locator_login = (By.ID,'submit') #登录按钮定位
    locator_success = (By.XPATH,'//a[text()="班级情况"]') #登录成功信息定位
    locator_fail = (By.CSS_SELECTOR,'.bootstrap-dialog-message') #登录失败信息定位
    locator_remember_me = (By.CSS_SELECTOR,'.remenber') #记住我定位
    locator_register = (By.CSS_SELECTOR,'.sign_in') #注册按钮定位
    locator_forget_passwd = (By.CSS_SELECTOR,'.forget_password') #忘记密码按钮定位
    loc_enter_register_succeess = (By.XPATH,'//h3[text()="老师注册"]') #进入注册页面成功，“老师注册”定位
    loc_enter_forget_success = (By.XPATH,"//h3[text()='找回密码']") #进入忘记密码页面成功，

    '''注册界面定位'''
    locator_teacher_name = (By.CSS_SELECTOR,'.realname') # 输入姓名对话框定位
    locator_input_phone = (By.CSS_SELECTOR,'.telephone') # 输入手机号对话框定位
    locator_yanzhengma  = (By.CSS_SELECTOR,'.verify') #验证码对话框定位
    locator_get_yanzhengma = (By.CSS_SELECTOR,'.gain_verify') #获取验证码定位
    locator_passwd = (By.CSS_SELECTOR,'.password') #密码框定位
    locator_queren_passwd = (By.CSS_SELECTOR,'.affirm-password') #确认密码定位
    locator_register_button = (By.CSS_SELECTOR,'.sign-in-btn') #注册按钮定位
    loc_not_input_phone = (By.CSS_SELECTOR,'span.hint.telephone-hint')#不输入手机号注册提示信息定位
    loc_input_error_phone = (By.CSS_SELECTOR,'span.hint.telephone-hint')#输入错误格式手机号注册提示信息定位
    loc_not_input_yanzhengma = (By.CSS_SELECTOR,'span.hint.verify-hint')#不输入验证码注册提示信息定位
    loc_input_error_yanzhengma = (By.CSS_SELECTOR,'.bootstrap-dialog-message')#输入错误验证码注册提示信息定位
    loc_not_input_passwd = (By.CSS_SELECTOR,'.hint.password-hint')#不输入密码及输入少于6位密码注册提示信息定位
    loc_not_same_passwd = (By.CSS_SELECTOR,'.hint.affirm-hint')#两次密码输入不一致注册提示信息定位

    '''个人信息界面定位'''
    loc_username = (By.CSS_SELECTOR,'.dropdown-toggle') #用户名称“霖”定位
    loc_person_infor = (By.CSS_SELECTOR,'.fa.fa-user') # 个人信息定位
    loc_base_infor = (By.XPATH,"//div[text()='您的基本信息']") #您的基本信息定位
    loc_change_base_infor = (By.XPATH,"//a[text()='基本信息修改']") #基本信息修改定位
    loc_choose_heard = (By.XPATH,"//a[text()='选择头像']") #选择头像定位
    # 用户信息修改成功、用户名不能为空、您没有修改信息、缺少新手机的验证码、错误 : 手机验证码不正确、
    # 错误 : 原密码错误、请输入新密码！！、请输入当前使用的密码！！、
    # 新密码和确认密码不同！、用户密码修改成功，点击确定，重新登录 定位
    loc_tishi = (By.CSS_SELECTOR,".bootstrap-dialog-message")
    loc_tishi_queding = (By.CSS_SELECTOR,'.btn.btn-default') #提示界面确定按钮
    loc_realname = "input[placeholder='真实姓名']" #真实姓名框定位
    loc_phone_num = "input[placeholder='手机号码']" #手机号码框定位
    #确定按钮定位
    loc_quedin = "td[colspan='2']>div.col-md-offset-3.col-md-9>button.btn.btn-primary"
    loc_yanzhengma = "input[ng-model='smscode.new']" #手机号验证码框定位
    loc_change_login_pwd = (By.XPATH,"//a[text()='登录密码修改']") #登录密码修改定位
    loc_mypasswd = "input[ng-model='MyPassWord']"#当前密码定位
    loc_change_pwd = "input[ng-model='MyNewPassWord1']" #修改密码定位
    loc_queren_pwd = "input[ng-model='MyNewPassWord2']" #确认密码定位
    loc_queding = "button[ng-click='modification_teacher_password();']" #确定按钮定位