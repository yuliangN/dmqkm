import allure
import pytest

from api.setting_api import Settings
from datas.read_yaml import users


@allure.feature("绑定邮箱页面")
class TestBindEmail:

    def setup_class(self):
        self.settings = Settings()

    @allure.story("发送邮箱成功-邮箱格式正确")
    @pytest.mark.parametrize('data', users.read_user()['email1'])
    def test_send_bind(self, user, data):
        r = self.settings.send_bind_email(user, data)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("发送邮箱失败-邮箱已绑定")
    @pytest.mark.parametrize('data', users.read_user()['email2'])
    def test_send_is_bind(self, user, data):
        r = self.settings.send_bind_email(user, data)
        assert r.get('code') == 11027
        assert r.get('message') == '该邮箱已绑定，请更换邮箱'

    @allure.story("发送邮箱失败-不符合邮箱格式规范")
    @pytest.mark.parametrize('data', users.read_user()['email3'])
    def test_send_format(self, user, data):
        r = self.settings.send_bind_email(user, data)
        assert r.get('code') == 11025
        assert r.get('message') == '邮箱格式错误'

    @allure.story("发送邮箱失败-邮箱为空")
    @pytest.mark.parametrize('data', users.read_user()['email4'])
    def test_send_null(self, user, data):
        r = self.settings.send_bind_email(user, data)
        assert r.get('code') == 25005
        assert r.get('message') == '缺少参数email'

    @allure.story("发送邮箱失败-邮箱存在中文")
    @pytest.mark.parametrize('data', users.read_user()['email5'])
    def test_send_text(self, user, data):
        r = self.settings.send_bind_email(user, data)
        assert r.get('code') == 11025
        assert r.get('message') == '邮箱格式错误'
