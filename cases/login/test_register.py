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

    # def teardown_class(self):
    #     pass

    @allure.story("手机号注册成功")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data7'])
    def test_registerSucceed(self, mobile):
        r = self.register.registerSucceed(mobile)
        assert r.get('code') == 1

    @allure.story("手机号注册失败-手机号格式不正确")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data6'])
    def test_registerFail_format(self, mobile):
        r = self.register.registerFail_format(mobile)
        assert r.get('code') == 11017
        assert r.get('message') == '手机号格式错误'

    @allure.story("手机号注册失败-手机号已存在")
    @pytest.mark.parametrize('mobile', Yamls().read_user()['data7'])
    def test_registerFail_exist(self, mobile):
        r = self.register.registerFail_exist(mobile)
        assert r.get('code') == 11019
        assert r.get('message') == '该手机号已注册，请直接登录或更换手机号！'
