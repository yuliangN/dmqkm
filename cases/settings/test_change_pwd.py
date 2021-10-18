# -*- coding:utf-8 -*-
import allure
import pytest
from api.setting_api import Settings


@allure.feature("修改密码页面")
class TestBindEmail:

    def setup_class(self):
        self.settings = Settings()

    @pytest.mark.run(order=2)
    @allure.story("修改成功-新老密码正确")
    def test_change_pwd(self, pwd_user):
        r = self.settings.change_password(pwd_user, '123qwe', '123qwe')
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @pytest.mark.run(order=1)
    @allure.story("修改失败-原密码错误")
    def test_oldpwd_error(self, pwd_user):
        r = self.settings.change_password(pwd_user, 'qwe123', '123qwe')
        assert r.get('code') == 11014
        assert r.get('message') == '原密码输入错误'

    # @allure.story("修改失败-新密码包含特殊字符")
    # def test_newpwd_error(self, pwd_user):
    #     r = self.settings.change_password(pwd_user, '@@##$', '123qwe')
    #     assert r.get('code') == 11015
    #     assert r.get('message') == '新密码包含特殊字符'
    #
    # @allure.story("修改失败-新密码长度不足")
    # def test_newpwd_length(self, pwd_user):
    #     r = self.settings.change_password(pwd_user, '12312', '123qwe')
    #     assert r.get('code') == 11016
    #     assert r.get('message') == '新密码长度不足'
    #
    # @allure.story("修改失败-新密码纯字符或纯数字")
    # def test_newpwd_length(self, pwd_user):
    #     r = self.settings.change_password(pwd_user, '123qwe', '123121')
    #     assert r.get('code') == 11017
    #     assert r.get('message') == '新密码纯字符或纯数字'
    #
