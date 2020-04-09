'''
   个人信息测试数据
'''

class PerInforDatas:
    '''基本信息修改数据'''
    #个人信息展示断言
    perinfor_show = {"expect":"您的基本信息"}
    #正常修改用户名
    change_user = {"realname":"霖",
                  "phone":17774571997,
                  "expect":"用户信息修改成功"}
    #用户名为空
    empty_name = {"realname":"",
                  "phone":17774571997,
                  "expect":"用户名不能为空"}
    #正常修改手机号
    change_phone = {"realname":"霖霖",
                    "phone":14760701301,
                    "expect":"用户信息修改成功"}
    #手机号为空
    empty_phone = {"realname":"霖霖",
                   "phone":"",
                   "expect":"您没有修改信息"}
    #验证码为空
    empty_yanzhengma = {"realname":"霖霖",
                        "phone":14760701301,
                        "yanzhengma": "",
                        "expect":"缺少新手机的验证码"}
    #输入错误的验证码
    input_error_yanzhengma = {"realname":"霖霖",
                              "phone":14760701301,
                              "yanzhengma": "2123",
                              "expect":"错误 : 手机验证码不正确"}

    '''登录密码修改'''
    #正常修改登录密码
    normal_change_pwd = {"current_pwd":"lnbx-94963",
                         "change_pwd":"123456789",
                         "same_pwd":"123456789",
                         "expect":"用户密码修改成功，点击确定，重新登录"}
    #原密码错误
    error_current_pwd = {"current_pwd":"lnbx9963",
                         "change_pwd":"123456789",
                         "same_pwd":"123456789",
                         "expect":"错误 : 原密码错误、请输入新密码！！"}
    #原密码为空
    empty_current_pwd = {"current_pwd":"",
                         "change_pwd":"123456789",
                         "same_pwd":"123456789",
                         "expect":"请输入当前使用的密码！！"}
    #新密码和确认密码为空
    empt_change_pwd = {"current_pwd":"lnbx-94963",
                       "change_pwd":"",
                       "same_pwd":"",
                       "expect":"请输入新密码！！"}
    #两次密码输入不一致
    not_same_pwd = {"current_pwd":"lnbx-94963",
                    "change_pwd":"12345",
                    "same_pwd":"656",
                    "expect":"新密码和确认密码不同！"}

