'''
   YJYX登录测试用例
'''
import pytest
import allure
import time
from YJYX_web_test.test_datas.login_datas import PhoneDatas as PD
from YJYX_web_test.common import log_test

@pytest.mark.usefixtures("set_updown_class_login")
@pytest.mark.usefixtures("set_updown_login")
class TestLogin:

    @pytest.mark.smoke1
    def test_login1(self,set_updown_class_login):
        '''正常登录测试'''
        log_test.get_logger("开始测试：{}".format(PD.normal_datas))
        set_updown_class_login[1].login(PD.normal_datas["username"],PD.normal_datas["password"])
        expect = set_updown_class_login[1].login_success()
        assert expect == PD.normal_datas["expect"]
        log_test.get_logger("获取的断言信息：{}".format(expect))
        log_test.get_logger("测试结束！")

    @pytest.mark.parametrize("data", PD.fail_datas)
    @pytest.mark.smoke1
    def test_login2(self, set_updown_class_login, data):
        '''异常登录测试'''
        log_test.get_logger("开始测试：{}".format(data))
        set_updown_class_login[1].login(data["username"], data["password"])
        expect = set_updown_class_login[1].login_fail()
        assert expect == data["expect"]
        log_test.get_logger("获取的断言信息：{}".format(expect))
        log_test.get_logger("测试结束！")

if __name__ == '__main__':
    pytest.main()