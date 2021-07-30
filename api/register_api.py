# 手机号注册模块
from lib.api_template import ApiTemplate


class RegisterApi:

    # 注册成功
    def registerSucceed(self, mobile):
        path = '/acc/v1/reg'
        data = {"mobile": mobile, "password": "qwe123",
                "sign": "daimaqiankun.sign", "deviceId": "15615615616",
                "osType": "09", "adId": 8001
                }
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    # 注册失败-手机号格式不正确
    def registerFail_format(self, mobile):
        path = '/acc/v1/reg'
        data = {"mobile": mobile, "password": "qwe123",
                "sign": "daimaqiankun.sign", "deviceId": "15615615616",
                "osType": "09", "adId": 8001
                }
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    # 注册失败-手机号已存在
    def registerFail_exist(self, mobile):
        path = '/acc/v1/reg'
        data = {"mobile": mobile, "password": "qwe123",
                "sign": "daimaqiankun.sign", "deviceId": "15615615616",
                "osType": "09", "adId": 8001
                }
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json
