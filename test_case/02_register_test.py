'''
   YJYX注册测试用例
'''
import pytest
import allure
import time
from YJYX_web_test.test_datas.register_datas import RegisterDatas as RD
from YJYX_web_test.common.log_test import get_logger

@pytest.mark.usefixtures("set_updown_class_register")
@pytest.mark.usefixtures("set_updown_register")
class TestRegister:

    @pytest.mark.smoke0
    def test_register_success01(self,set_updown_class_register):
        '''只输入必填项成功注册'''
        get_logger("测试开始：{}".format(RD.register_success01))
        set_updown_class_register[1].register(RD.register_success01["teachername"],
                                              RD.register_success01["phone"],
                                              RD.register_success01["yanzhengma"],
                                              RD.register_success01["pwd"],
                                              RD.register_success01["qrpwd"])
        expect = set_updown_class_register[1].register_success()
        assert expect == RD.register_success01["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    def test_register_success02(self0,set_updown_class_register):
        '''所有信息全部填写注册'''
        get_logger("测试开始：{}".format(RD.register_success02))
        set_updown_class_register[1].register(RD.register_success02["teachername"],
                                              RD.register_success02["phone"],
                                              RD.register_success02["yanzhengma"],
                                              RD.register_success02["pwd"],
                                              RD.register_success02["qrpwd"])
        expect = set_updown_class_register[1].register_success()
        assert expect == RD.register_success02["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    def test_not_input_phone(self,set_updown_class_register):
        '''不输入手机号注册'''
        get_logger("测试开始：{}".format(RD.not_input_phone))
        set_updown_class_register[1].register(RD.not_input_phone["teachername"],
                                              RD.not_input_phone["phone"],
                                              RD.not_input_phone["yanzhengma"],
                                              RD.not_input_phone["pwd"],
                                              RD.not_input_phone["qrpwd"])
        expect = set_updown_class_register[1].not_input_phone()
        assert expect == RD.not_input_phone["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    @pytest.mark.parametrize("data",RD.input_error_phone)
    def test_input_error_phone(self,set_updown_class_register,data):
        '''输入错误格式手机号注册'''
        get_logger("测试开始：{}".format(data))
        set_updown_class_register[1].register(data["teachername"],
                                              data["phone"],
                                              data["yanzhengma"],
                                              data["pwd"],
                                              data["qrpwd"])
        expect = set_updown_class_register[1].input_error_phone()
        assert expect == data["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    def test_not_input_yanzhengma(self,set_updown_class_register):
        '''不输入验证码注册'''
        get_logger("测试开始：{}".format(RD.not_input_yanzhengma))
        set_updown_class_register[1].register(RD.not_input_yanzhengma["teachername"],
                                              RD.not_input_yanzhengma["phone"],
                                              RD.not_input_yanzhengma["yanzhengma"],
                                              RD.not_input_yanzhengma["pwd"],
                                              RD.not_input_yanzhengma["qrpwd"])
        expect = set_updown_class_register[1].not_input_yanzhengma()
        assert expect == RD.not_input_yanzhengma["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    def test_input_error_yanzhengma(self,set_updown_class_register):
        '''输入错误验证码注册'''
        get_logger("测试开始：{}".format(RD.input_error_yanzhengma))
        set_updown_class_register[1].register(RD.input_error_yanzhengma["teachername"],
                                              RD.input_error_yanzhengma["phone"],
                                              RD.input_error_yanzhengma["yanzhengma"],
                                              RD.input_error_yanzhengma["pwd"],
                                              RD.input_error_yanzhengma["qrpwd"])
        expect = set_updown_class_register[1].input_error_yanzhengma()
        assert expect == RD.input_error_yanzhengma["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    @pytest.mark.parametrize("data",RD.not_input_pwd)
    def test_not_input_pwd(self,set_updown_class_register,data):
        '''不输入密码及输入少于6位密码注册'''
        get_logger("测试开始：{}".format(data))
        set_updown_class_register[1].register(data["teachername"],
                                              data["phone"],
                                              data["yanzhengma"],
                                              data["pwd"],
                                              data["qrpwd"])
        expect = set_updown_class_register[1].not_input_pwd()
        assert expect == data["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

    @pytest.mark.smoke0
    def test_not_same_phone(self,set_updown_class_register):
        '''两次密码输入不一致注册'''
        get_logger("测试开始：{}".format(RD.not_same_pwd))
        set_updown_class_register[1].register(RD.not_same_pwd["teachername"],
                                              RD.not_same_pwd["phone"],
                                              RD.not_same_pwd["yanzhengma"],
                                              RD.not_same_pwd["pwd"],
                                              RD.not_same_pwd["qrpwd"])
        expect = set_updown_class_register[1].not_same_pwd()
        assert expect == RD.not_same_pwd["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束")

if __name__ == '__main__':
    pytest.main()

