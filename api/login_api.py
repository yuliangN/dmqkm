from lib.api_template import ApiTemplate

# 手机号登录模块
class Login:
    # 获取token
    def get_token(self):
        path = '/acc/v1/login/password'
        data = {"accountName": "13911111015", "password": "qwe123",
                "sign": "daimaqiankun.sign", "deviceId": "15615615616",
                "osType": "09",
                "adId": 8001}
        res_json = ApiTemplate().post_api(path, data)
        return res_json.get('token')

    # 手机号登录
    def login(self, mobile, pwd):
        path = '/acc/v1/login/password'
        data = {"accountName": mobile,
                "password": pwd,
                "sign": "daimaqiankun.sign",
                "deviceId": "15615615616",
                "osType": "09",
                "adId": 8001}
        res_json = ApiTemplate().post_api(path, data)
        return res_json

    # 密码特殊符号
    def loginfail_symbol(self, mobile):
        path = '/acc/v1/login/password'
        data = {"accountName": mobile,
                "password": "@%^&#%^&",
                "sign": "daimaqiankun.sign",
                "deviceId": "15615615616",
                "osType": "09",
                "adId": 8001}
        res_json = ApiTemplate().post_api(path, data)
        return res_json

    # 密码为空
    def loginfail_empty(self, mobile):
        path = '/acc/v1/login/password'
        data = {"accountName": mobile,
                "password": "      ",
                "sign": "daimaqiankun.sign",
                "deviceId": "15615615616",
                "osType": "09",
                "adId": 8001}
        res_json = ApiTemplate().post_api(path, data)
        return res_json

# if __name__ == '__main__':
#     print(Login().get_token())
