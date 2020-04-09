'''
   登录测试数据
'''
class PhoneDatas:
    normal_datas = {"username":17774571997,"password":"lnbx-94963","expect":"班级情况"} #正确手机号和密码

    fail_datas =  [{"username":17774571997,"password":"lnbx94963","expect":"登录失败 : 用户名或密码错误"},  #正确手机号和错误密码
                   {"username":1777457199788,"password": "lnbx-94963","expect":"登录失败 : 用户名或密码错误"}, #手机号大于11位和正确密码
                   {"username":17774571,"password": "lnbx94963","expect":"登录失败 : 用户名或密码错误"}, #手机号小于11位和正确密码
                   {"username":27774571997,"password": "lnbx94963","expect":"登录失败 : 用户名或密码错误"}, #手机号不在号段和正确密码
                   {"username":"","password": "lnbx94963","expect":"登录失败 : 用户名或密码错误"}, #用户名为空和正确密码
                   {"username":17774571997,"password": "","expect":"登录失败 : 用户名或密码错误"}] #正确用户名和密码为空


