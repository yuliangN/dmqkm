# -*- coding:utf-8 -*-
import pytest

from api.login_api import Login


@pytest.fixture(scope='class')
def user():
    token = Login().get_token()
    return token
