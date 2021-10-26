# -*- coding:utf-8 -*-
import pytest

from api.login_api import Login


@pytest.fixture('module')
def user():
    token = Login().get_token()
    return token


@pytest.fixture(scope='module')
def pwd_user():
    token = Login().change_pwd_token()
    return token
