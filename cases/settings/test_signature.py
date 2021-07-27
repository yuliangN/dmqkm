from api.setting_api import Settings
import allure


@allure.feature("修改签名页面")
class TestSignnature:
    # 初始化设置页
    def setup_class(self):
        self.settings = Settings()

    @allure.feature("修改成功签名-数字")
    def test_change_signature(self, user):
        r = self.settings.changeSignature(user)
        assert  r.get('code') == 1
        assert  r.get('message') == '操作成功'

    @allure.feature("修改成功签名-文字")
    def test_change_letter(self, user):
        r = self.settings.changeSignatureletter(user)
        assert  r.get('code') == 1
        assert  r.get('message') == '操作成功'

    @allure.feature("修改成功签名-特殊符号")
    def test_change_symbol(self, user):
        r = self.settings.changeSignatureSymbol(user)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.feature("修改签名失败-敏感字")
    def test_symbol(self, user):
        r = self.settings.changeSignaFail(user)
        assert r.get('code') == 11057