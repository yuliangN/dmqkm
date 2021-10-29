import pytest
import allure

from api.register_api import RegisterApi
from datas.read_yaml import Yamls
from lib.config_sql import DB


@allure.feature("注册页")
class TestRegister:

    def setup_class(self):
        self.register = RegisterApi()
        DB.del_mobile(Yamls().read_user()['data5'])

    @allure.story("手机号注册成功")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data10'])
    def test_register_succeed(self, mobile):
        r = self.register.register(mobile)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("手机号注册失败-手机号为10位数字")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data6'])
    def test_registerFail_format(self, mobile):
        r = self.register.register(mobile)
        assert r.get('code') == 11017
        assert r.get('message') == '手机号格式错误'

    @allure.story("手机号注册失败-手号包含特殊符号")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data8'])
    def test_joint_letter(self, mobile):
        r = self.register.register(mobile)
        assert r.get('code') == 11017
        assert r.get('message') == '手机号格式错误'

    @allure.story("发送验证码-手机号已存在")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data7'])
    def test_registerFail_exist(self, mobile):
        r = self.register.registerFail_exist(mobile)
        assert r.get('code') == 11019
        assert r.get('message') == '该手机号已注册，请直接登录或更换手机号！'

    # @allure.story("验证码校验失败-验证码已过期")
    # @pytest.mark.parametrize('mobile', Yamls().read_user()['data7'])
    # def test_code_expire(self, mobile):
    #     r = self.register.text_message(mobile)
    #     assert r.get('code') == 11035
    #     assert r.get('message') == '验证码已过期'

    @allure.story("验证码校验失败-手机号未发送验证码")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data9'])
    def test_code_exist(self, mobile):
        r = self.register.text_message(mobile)
        assert r.get('code') == 11033
        assert r.get('message') == '验证码输入错误'

    @allure.story("发送验证码成功")
    def test_code_succeed(self, phone):
        r = self.register.registerFail_exist(phone)
        assert r.get('code') == 1
        assert r.get('sms') == '6666' and r.get('message') == '操作成功'

    @allure.story("验证码校验成功")
    def test_checkout_succeed(self, phone):
        r = self.register.registerFail_exist(phone)
        r = self.register.text_message(phone)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'
