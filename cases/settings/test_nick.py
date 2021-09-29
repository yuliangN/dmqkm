import pytest

from api.setting_api import Settings
import allure


@allure.feature("修改昵称页面")
class TestNick:
    # 初始化设置页
    def setup_class(self):
        self.settings = Settings()
    @allure.story("修改失败-昵称敏感字")
    def test_nick_sensitive(self, user):
        r = self.settings.nickSensitiveWord(user)
        assert r.get('code') == 11057

    @allure.story("修改失败-昵称为空（后端未做校验）")
    def test_nick_null(self, user):
        r = self.settings.nickNull(user)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("修改成功昵称")
    def test_success_nick(self, user):
        r = self.settings.change_nick(user)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("修改失败-昵称已存在")
    def test_nick_exist(self, user):
        r = self.settings.nickExist(user)
        assert r.get('code') == 11022
        assert r.get('message') == '昵称已存在'
