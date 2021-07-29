import pytest
import allure
from api.login_api import Login
from datas.read_yaml import Yamls

@allure.feature("登录页")
class TestLogin:
    # 初始化用户登录
    def setup_class(self):
        self.login = Login()

    # 手机号登录成功，参数化+数据驱动 获取手机号及密码
    @allure.story("手机号登录成功")
    @pytest.mark.parametrize('param1,param2', Yamls().read_user()['data'])
    def test_login_succeed(self, param1, param2):
        r = self.login.login(param1, param2)
        assert r.get('code') == 1

    @allure.story("手机号登录失败-密码纯英文")
    @pytest.mark.parametrize('param1,param2', Yamls().read_user()['data2'])
    def test_loginfail_letter(self, param1, param2):
        r = self.login.login(param1, param2)
        assert r.get('code') == 11011

    @allure.story("手机号登录失败-密码纯数字")
    @pytest.mark.parametrize('param1,param2', Yamls().read_user()['data3'])
    def test_loginfail_figure(self, param1, param2):
        r = self.login.login(param1, param2)
        assert r.get('code') == 11011

    @allure.story("手机号登录失败-密码特殊符号")
    @pytest.mark.parametrize('param1', Yamls().read_user()['data4'])
    def test_loginfail_symbol(self, param1):
        r = self.login.loginfail_symbol(param1)
        assert r.get('code') == 11011

    @allure.story("手机号登录失败-密码为空")
    @pytest.mark.parametrize('param1', (Yamls().read_user()['data4']))
    def test_loginfail_empty(self, param1):
        r = self.login.loginfail_empty(param1)
        assert r.get('code') == 25005
