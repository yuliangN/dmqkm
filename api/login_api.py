from lib.api_template import ApiTemplate
from lib.log_api import log
from datas.read_yaml import users


# 手机号登录模块
class Login:

    # 获取token
    def get_token(self):
        path = '/acc/v1/login/password'
        data = {"accountName": users.read_yml()['public']['mobile'],
                "password": "qwe123",
                "sign": users.read_yml()['public']['sign'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "osType": users.read_yml()['public']['osType'],
                "adId": users.read_yml()['public']['adId']}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"获取用户token: {res_json.get('token')}")
        return res_json.get('token')

    # 获取修改密码的token用户
    def change_pwd_token(self):
        path = '/acc/v1/login/password'
        data = {"accountName": 13911111521,
                "password": '123qwe',
                "sign": users.read_yml()['public']['sign'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "osType": users.read_yml()['public']['osType'],
                "adId": users.read_yml()['public']['adId']}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"获取用户token: {res_json.get('token')}")
        return res_json.get('token')

    # 手机号登录
    def login(self, mobile, pwd):
        path = '/acc/v1/login/password'
        data = {"accountName": mobile,
                "password": pwd,
                "sign": users.read_yml()['public']['sign'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "osType": users.read_yml()['public']['osType'],
                "adId": users.read_yml()['public']['adId']}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 密码特殊符号
    def loginfail_symbol(self, mobile):
        path = '/acc/v1/login/password'
        data = {"accountName": mobile,
                "password": "@%^&#%^&",
                "sign": users.read_yml()['public']['sign'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "osType": users.read_yml()['public']['osType'],
                "adId": users.read_yml()['public']['adId']}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 密码为空
    def loginfail_empty(self, mobile):
        path = '/acc/v1/login/password'
        data = {"accountName": mobile,
                "password": "      ",
                "sign": users.read_yml()['public']['sign'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "osType": users.read_yml()['public']['osType'],
                "adId": users.read_yml()['public']['adId']}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

# if __name__ == '__main__':
#     print(Login().get_token())
