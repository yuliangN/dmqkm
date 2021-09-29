import allure
import pytest

from datas.read_yaml import Yamls
from api.setting_api import Settings
from lib.config_sql import DB


@allure.feature("实名页面")
class TestAutonym:
    # 实例化读取实名信息
    autonym = Yamls().read_user()

    def setup_class(self):
        self.settings = Settings()
        DB.init_autonym(Yamls().read_yml()['public']['selfUserCode'])

    @allure.story("成功-实名认证")
    @pytest.mark.parametrize('name,idcard', autonym['users'])
    def test_autonym(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("失败-身份证号错误")
    @pytest.mark.parametrize('name,idcard', autonym['users1'])
    def test_idcard_error(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 11041
        assert r.get('message') == '认证失败，该真实姓名和身份证不匹配'

    @allure.story("失败-身份证号类型错误")
    @pytest.mark.parametrize('name,idcard', autonym['users2'])
    def test_idcard_type_error(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 11041
        assert r.get('message') == '认证失败，该真实姓名和身份证不匹配'

    @allure.story("失败-姓名不正确")
    @pytest.mark.parametrize('name,idcard', autonym['users3'])
    def test_name_error(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 11041
        assert r.get('message') == '认证失败，该真实姓名和身份证不匹配'

    @allure.story("失败-姓名为空")
    @pytest.mark.parametrize('name,idcard', autonym['users4'])
    def test_name_null(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 25005
        assert r.get('message') == '缺少参数name'

    @allure.story("失败-手机号为空")
    @pytest.mark.parametrize('name,idcard', autonym['users5'])
    def test_mobile_null(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 25005
        assert r.get('message') == '缺少参数idcard'

    @allure.story("失败-手机号为空")
    @pytest.mark.parametrize('name,idcard', autonym['users6'])
    def test_mobile_char(self, user, name, idcard):
        r = self.settings.autonym(user, name, idcard)
        assert r.get('code') == 11041
        assert r.get('message') == '认证失败，该真实姓名和身份证不匹配'