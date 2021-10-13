
from lib.api_template import ApiTemplate
from lib.log_api import log
from datas.read_yaml import users


# 设置模块
class Settings:

    # 成功-修改昵称
    def change_nick(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "nick": "大宝贝"}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 失败-昵称已存在
    def nickExist(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "nick": "机会"}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 失败-昵称敏感词
    def nickSensitiveWord(self, data):
        print(data)
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "nick": "操"}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 失败-昵称为空
    def nickNull(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "nick": " "}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 成功-修改用户签名数字
    def changeSignature(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "introduction": "6666"}
        res_json = ApiTemplate().post_api(path,data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 成功 - 修改用户签名文字
    def changeSignatureletter(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "introduction": "来吧"}
        res_json = ApiTemplate().post_api(path,data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 成功 - 修改用户签名特殊符号
    def changeSignatureSymbol(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "introduction": "@#￥%……A&"}
        res_json = ApiTemplate().post_api(path,data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 失败-签名敏感字校验
    def changeSignaFail(self, data, datas):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "introduction": datas}
        res_json = ApiTemplate().post_api(path,data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 成功-修改性别
    def change_gender(self, data, parme):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "gender": parme}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 成功-性别为空
    def change_genderfail(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "gender": "nn"}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 实名
    def autonym(self, data, name, idcard):
        path = '/acc/v1/profile/identity'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "name": name,
                "idcard": idcard}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 发送邮箱
    def send_bind_email(self, user, data):
        path = '/acc/v1/send-sms/bind/email'
        data = {"token": user,
                "email": data,
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回参数 : {res_json}")
        return res_json

    # 绑定邮箱
    def bind_email(self, data, email):
        path = '/acc/v1/bind/email'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "code": 6666,
                "email": email
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回参数 : {res_json}")
        return res_json
