import pytest

from api.login_api import Login


# 初始化，获取token
@pytest.fixture(scope='class')
def user():
    token = Login().get_token()
    return token

