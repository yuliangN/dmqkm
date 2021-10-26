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

    @allure.story("修改失败-昵称敏感字")
    @pytest.mark.parametrize('param', users.read_personal()['nick'])
    def test_nick_sensitive(self, user, param):
        r = self.settings.nickSensitiveWord(user, param)
        assert r.get('code') == 11057

    @allure.story("修改失败-昵称为空（后端未做校验）")
    def test_nick_null(self, user):
        r = self.settings.nickNull(user)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("修改成功-昵称")
    @pytest.mark.parametrize('param1', users.read_personal()['region5'])
    def test_success_nick(self, user, param1):
        r = self.settings.change_nick(user, param1)
        assert r.get('code') == 1
        assert r.get('profile')['nick'] == ''.join(param1)

    @allure.story("修改失败-昵称已存在")
    def test_nick_exist(self, user):
        r = self.settings.nickExist(user)
        assert r.get('code') == 11022
        assert r.get('message') == '昵称已存在'

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

    @allure.story("出生日期设置成功-输入有效的日期")
    @pytest.mark.parametrize('param1', users.read_personal()['region3'])
    def test_birth_succeed(self, user, param1):
        r = self.settings.set_birth_data(user, param1)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("出生日志设置失败-日期格式不正确")
    @pytest.mark.parametrize('param1', users.read_personal()['region4'])
    def test_birth_format_error(self, user, param1):
        r = self.settings.set_birth_data(user, param1)
        assert r.get('code') == 25009
        assert r.get('message') == 'birth格式错误'

    @allure.story('成功-修改性别')
    @pytest.mark.parametrize('parme', ['m', 'f', ' '])
    def test_gender(self, user, parme):
        r = self.settings.change_gender(user, parme)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story('失败-参数其他类型 非m,f')
    def test_gender_fail(self, user):
        r = self.settings.change_genderfail(user)
        assert r.get('code') == 10001
