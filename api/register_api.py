# 手机号注册模块
from lib.api_template import ApiTemplate
from lib.log_api import log
from datas.read_yaml import users


class RegisterApi:

    # 注册成功
    def register(self, mobile):
        path = '/acc/v1/reg'
        data = {"mobile": mobile,
                "password": "qwe123",
                "sign": "daimaqiankun.sign",
                "deviceId": "15615615616",
                "osType": "09",
                "lang": users.read_yml()['public']['lang'],
                "adId": 8001
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    #  验证码校验
    def registerFail_exist(self, mobile):
        path = '/acc/v1/send-sms/reg'
        data = {"mobile": mobile,
                "sign": "daimaqiankun.sign",
                "lang": users.read_yml()['public']['lang'],
                "deviceId": "15615615616"}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 短信验证
    def text_message(self, mobile):
        path = '/acc/v1/checkcode'
        data = {"mobile": mobile,
                "sign": "daimaqiankun.sign",
                "deviceId": "15615615616",
                "code": "6666",
                "lang": users.read_yml()['public']['lang'],
                "flag": "reg"}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json
