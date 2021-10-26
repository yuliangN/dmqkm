# import pytest
#
# from api.login_api import Login
#
#
# # 初始化，获取token
# @pytest.fixture(scope='class')
# def user():
#     token = Login().get_token()
#     return token
#
#
# # 获取修改用户的token
# @pytest.fixture(scope='class')
# def pwd_user():
#     token = Login().change_pwd_token()
#     return token
