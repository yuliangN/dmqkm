
from lib.api_template import ApiTemplate
from lib.gain_files import GainFiles
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

    # 反馈与建议纯文本
    def feedback_text(self, data, param1, param2, param3):
        path = '/review/faceback/insert'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "type": param1,
                "contactWay": param3,
                "content": param2
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回参数 : {res_json}")
        return res_json

        # 反馈与建议上传图片
    def feedback_image(self, data, param1, param2, param3, image):
        path = '/review/faceback/insert'
        files = GainFiles().gain_images(image)
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "type": param1,
                "contactWay": param3,
                "content": param2
                }
        res_json = ApiTemplate().post_api(path, data, files=files)
        log.info(f"接口返回参数 : {res_json}")
        return res_json

        # 反馈与建议上传图片
    def feedback_more_image(self, data, param1, param2, param3):
        path = '/review/faceback/insert'
        files = GainFiles().gain_more_images()
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "type": param1,
                "contactWay": param3,
                "content": param2
                }
        res_json = ApiTemplate().post_api(path, data, files=files)
        log.info(f"接口返回参数 : {res_json}")
        return res_json

    # 反馈与建议纯文本
    def feedback_text1(self, data, param1, param2, param3):
        path = '/review/faceback/insert'
        data = {"token": data,
                "selfUserCode": users.read_yml()['public']['selfUserCode'],
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "type": param1,
                "contactWay": param3,
                "content": param2
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回参数 : {res_json}")
        return res_json

    # 修改密码
    def change_password(self, data, param1, param2):
        path = '/acc/v1/password/modify'
        data = {"token": data,
                "selfUserCode": '27423001052446720',
                "deviceId": users.read_yml()['public']['deviceId'],
                "sign": users.read_yml()['public']['sign'],
                "lang": users.read_yml()['public']['lang'],
                "old": param1,
                "password": param2,
                "osType": users.read_yml()['public']['osType']
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回参数 : {res_json}")
        return res_json
