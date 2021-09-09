import allure
import pytest

from api.setting_api import Settings


@allure.feature("修改性别")
class TestGender:
    # 初始化设置页
    def setup_class(self):
        self.settings = Settings()

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