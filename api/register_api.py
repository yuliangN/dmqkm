# 手机号注册模块
from lib.api_template import ApiTemplate


class RegisterApi:

    # 注册成功
    def register(self, mobile):
        path = '/acc/v1/reg'
        data = {"mobile": mobile, "password": "qwe123",
                "sign": "daimaqiankun.sign", "deviceId": "15615615616",
                "osType": "09", "adId": 8001
                }
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    #  验证码校验
    def registerFail_exist(self, mobile):
        path = '/acc/v1/send-sms/reg'
        data = {"mobile": mobile, "sign": "daimaqiankun.sign", "deviceId": "15615615616"}
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    # 短信验证
    def text_message(self, mobile):
        path = '/acc/v1/checkcode '
        data = {"mobile": mobile, "sign": "daimaqiankun.sign", "deviceId": "15615615616",
                "code": "6666", "flag": "reg"}
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json
