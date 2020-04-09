'''
   个人信息页面测试用例
'''
import pytest
import allure
import time
from YJYX_web_test.test_datas.per_infor_datas import PerInforDatas as PID
from YJYX_web_test.common.log_test import get_logger

@pytest.mark.usefixtures("set_updown_class_perinfor")
@pytest.mark.usefixtures("set_updown_perinfor")
class TestPerInfor:

    @pytest.mark.per
    def test_per_infor_show(self,set_updown_class_perinfor):
        '''个人详细信息展示'''
        get_logger("测试开始！")
        expect = set_updown_class_perinfor[1].per_infor_assert()
        assert expect == PID.perinfor_show["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.per
    def test_change_user(self,set_updown_class_perinfor):
        '''正常修改用户名'''
        get_logger("测试开始：{}".format(PID.change_user))
        set_updown_class_perinfor[1].base_infor_change(PID.change_user["realname"],
                                                       PID.change_user["phone"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.change_user["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.per
    def test_empty_name(self,set_updown_class_perinfor):
        '''用户名为空'''
        get_logger("测试开始：{}".format(PID.empty_name))
        set_updown_class_perinfor[1].base_infor_change(PID.empty_name["realname"],
                                                       PID.empty_name["phone"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.empty_name["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.per
    def test_change_phone(self,set_updown_class_perinfor):
        '''正常修改手机号'''
        get_logger("测试开始：{}".format(PID.change_phone))
        set_updown_class_perinfor[1].base_infor_change(PID.change_phone["realname"],
                                                       PID.change_phone["phone"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.change_phone["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.per
    def test_empty_phone(self,set_updown_class_perinfor):
        '''手机号为空'''
        get_logger("测试开始：{}".format(PID.empty_phone))
        set_updown_class_perinfor[1].base_infor_change(PID.empty_phone["realname"],
                                                       PID.empty_phone["phone"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.empty_phone["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.pwd
    def test_error_current_pwd(self,set_updown_class_perinfor):
        '''原密码错误'''
        get_logger("测试开始：{}".format(PID.error_current_pwd))
        set_updown_class_perinfor[1].change_pwd(PID.error_current_pwd["current_pwd"],
                                                PID.error_current_pwd["change_pwd"],
                                                PID.error_current_pwd["same_pwd"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.error_current_pwd["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.pwd
    def test_empty_current_pwd(self,set_updown_class_perinfor):
        '''原密码为空'''
        get_logger("测试开始：{}".format(PID.empty_current_pwd))
        set_updown_class_perinfor[1].change_pwd(PID.empty_current_pwd["current_pwd"],
                                                PID.empty_current_pwd["change_pwd"],
                                                PID.empty_current_pwd["same_pwd"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.empty_current_pwd["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.pwd
    def test_empt_change_pwd(self,set_updown_class_perinfor):
        '''新密码和确认密码为空'''
        get_logger("测试开始：{}".format(PID.empt_change_pwd))
        set_updown_class_perinfor[1].change_pwd(PID.empt_change_pwd["current_pwd"],
                                                PID.empt_change_pwd["change_pwd"],
                                                PID.empt_change_pwd["same_pwd"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.empt_change_pwd["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.pwd
    def test_not_same_pwd(self,set_updown_class_perinfor):
        '''两次密码输入不一致'''
        get_logger("测试开始：{}".format(PID.not_same_pwd))
        set_updown_class_perinfor[1].change_pwd(PID.not_same_pwd["current_pwd"],
                                                PID.not_same_pwd["change_pwd"],
                                                PID.not_same_pwd["same_pwd"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.not_same_pwd["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

    @pytest.mark.pwd
    def test_normal_change_pwd(self,set_updown_class_perinfor):
        '''正常修改登录密码'''
        get_logger("测试开始：{}".format(PID.normal_change_pwd))
        set_updown_class_perinfor[1].change_pwd(PID.normal_change_pwd["current_pwd"],
                                                PID.normal_change_pwd["change_pwd"],
                                                PID.normal_change_pwd["same_pwd"])
        expect = set_updown_class_perinfor[1].tishi_infor()
        assert expect == PID.normal_change_pwd["expect"]
        get_logger("获取的断言信息：{}".format(expect))
        get_logger("测试结束！")

if __name__ == '__main__':
    pytest.main()
