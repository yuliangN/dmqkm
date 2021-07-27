import pytest

from api.login_api import Login
from datas.read_yaml import Yamls


class TestLogin:
    def setup_class(self):
        self.login = Login()

    # 手机号登录成功，参数化+数据驱动 获取手机号及密码
    @pytest.mark.parametrize('param1,param2', Yamls().read_user())
    def test_login_fail2(self, param1, param2):
        print(param1, param2)
        r = self.login.login(param1, param2)
        assert r.get('code') == 1
