# -*- coding:utf-8 -*-
import allure
import pytest
from datas.read_yaml import users
from api.setting_api import Settings


@allure.feature("个人资料页")
class TestPersonal:
    # 初始化设置页
    def setup_class(self):
        self.settings = Settings()

    @allure.story("地区设置成功-输入有效的地区名")
    @pytest.mark.parametrize('param1,param2', users.read_personal()['region'])
    def test_region_succeed(self, user, param1, param2):
        r = self.settings.set_region(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('profile')['province'] == param1 and r.get('profile')['city'] == param2

    @allure.story("地区设置成功-设置省份未设置市区")
    @pytest.mark.parametrize('param1,param2', users.read_personal()['region1'])
    def test_set_province(self, user, param1, param2):
        r = self.settings.set_region(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('profile')['province'] == param1

    @allure.story("地区设置成功-设置市区未设置身份")
    @pytest.mark.parametrize('param1,param2', users.read_personal()['region2'])
    def test_set_city(self, user, param1, param2):
        r = self.settings.set_region(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('profile')['city'] == param2

    # @allure.story("出生日期设置成功-输入有效的日期")
    # def test_birth_succeed(self):
    #     pass
    #
    # @allure.story("出生日志设置失败-日期格式不正确")
    # def test_birth_format_error(self):
    #     pass
