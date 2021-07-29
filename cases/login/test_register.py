import pytest
import allure

from api.register_api import RegisterApi
from lib.config_sql import DB


@allure.feature("注册页")
class TestRegister:
    def setup_class(self):
        self.register = RegisterApi()

    # def teardown_class(self):
    #     DB.del_mobile(13911111045)

    @allure.story("手机号注册成功")
    def test_registerSucceed(self):
        r = self.register.registerSucceed()
        assert r.get('code') == 1

    @allure.story("手机号注册失败-手机号格式不正确")
    def test_registerFail_format(self):
        pass

    @allure.story("手机号注册失败-手机号已存在")
    def test_registerFail_exist(self):
        pass
