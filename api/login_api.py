from api.base_api import BaseApi
import requests

from lib.api_template import ApiTemplate


class Login:
    # 获取token
    def get_token(self):
        path = '/acc/v1/login/password'
        data = {"accountName": "13911111015",
                              "password": "qwe123",
                              "sign": "daimaqiankun.sign",
                              "deviceId": "15615615616",
                              "osType": "09",
                "adId": 8001}
        res_json = ApiTemplate().post_api(path, data)
        # print(res_json)
        return res_json.get('token')

# if __name__ == '__main__':
#     print(Login().get_token())
