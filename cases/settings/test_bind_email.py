import allure
import pytest

from api.setting_api import Settings
from datas.read_yaml import users


@allure.feature("绑定邮箱页面")
class TestBindEmail:

    def setup_class(self):
        self.settings = Settings()

    @allure.story("发送邮箱成功-邮箱格式正确")
    @pytest.mark.parametrize('data', users.read_user()['eamail1'])
    def test_send_bind(self, user, data):
        r = self.settings.send_bind_email(user, data)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("发送邮箱失败-格式不正确")
    def test_send_format(self):
        pass

    @allure.story("发送邮箱失败-邮箱已绑定")
    def test_send_is_bind(self):
        pass

    def test01(self):
        print(users.read_user()['email3'])
