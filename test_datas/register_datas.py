'''
   注册测试数据
'''

class RegisterDatas:
    # 只输入必填项成功注册
    register_success01  = {"teachername":"",
                           "phone":14760701301,
                           "yanzhengma":"xxx",
                           "pwd":"lnbx-94963",
                           "qrpwd":"lnbx-94963",
                           "expect":"注册成功"}
    # 所有信息全部填写成功注册注册
    register_success02 = {"teachername": "零零七",
                          "phone": 14760701301,
                          "yanzhengma": "xxx",
                          "pwd": "lnbx-94963",
                          "qrpwd": "lnbx-94963",
                          "expect":"注册成功"}
    # 不输入手机号注册
    not_input_phone = {"teachername": "零零七",
                       "phone": "",
                       "yanzhengma": "xxx",
                       "pwd": "lnbx-94963",
                       "qrpwd": "lnbx-94963",
                       "expect": "请输入手机号码"}
    #输入错误格式手机号
    input_error_phone = [{"teachername": "零零七",
                         "phone": 24798569658,
                         "yanzhengma": "xxx",
                         "pwd": "lnbx-94963",
                         "qrpwd": "lnbx-94963",
                         "expect": "请输入正确的手机号码"},#输入手机号不在号段注册
                         {"teachername": "零零七",
                          "phone": 1479586,
                          "yanzhengma": "xxx",
                          "pwd": "lnbx-94963",
                          "qrpwd": "lnbx-94963",
                          "expect": "请输入正确的手机号码"}#输入手机号小于11位注册
                         ]
    #不输入验证码注册
    not_input_yanzhengma = {"teachername": "零零七",
                            "phone": 14760701301,
                            "yanzhengma": "",
                            "pwd": "lnbx-94963",
                            "qrpwd": "lnbx-94963",
                            "expect": "请输入验证码"}
    #输入错误验证码注册
    input_error_yanzhengma = {"teachername": "零零七",
                              "phone": 14760701301,
                              "yanzhengma": "xxx",
                              "pwd": "lnbx-94963",
                              "qrpwd": "lnbx-94963",
                              "expect": "验证码错误或超时，请重新获取"}
    #不输入密码注册及输入密码小于6位注册
    not_input_pwd = [{"teachername": "零零七",
                     "phone": 14760701301,
                     "yanzhengma": "xxx",
                     "pwd": "",
                     "qrpwd": "",
                     "expect": "密码至少6位字符"}, #不输入密码注册
                     {"teachername": "零零七",
                      "phone": 14760701301,
                      "yanzhengma": "xxx",
                      "pwd": "123",
                      "qrpwd": "123",
                      "expect": "密码至少6位字符"} #输入密码小于6位注册
                     ]
    #两次密码输入不一致注册
    not_same_pwd = {"teachername": "零零七",
                    "phone": 14760701301,
                    "yanzhengma": "xxx",
                    "pwd": "lnbx-94963",
                    "qrpwd": "lnbx94963",
                    "expect": "两次密码输入不一致"}