from api.setting_api import Settings


class TestSignnature:
    def setup_class(self):
        self.settings = Settings()

    # 修改成功签名-数字
    def test_change_signature(self, user):
        r = self.settings.changeSignature(user)
        assert  r.get('code') == 1
        assert  r.get('message') == '操作成功'

    # 修改成功签名-文字
    def test_change_letter(self):
        r = self.settings.changeSignatureletter()
        assert  r.get('code') == 1
        assert  r.get('message') == '操作成功'

    def test_change_symbol(self):
        r = self.settings.changeSignatureSymbol()
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    # 修改签名失败-敏感字
    def test_symbol(self):
        r = self.settings.changeSignaFail()
        assert r.get('code') == 11057