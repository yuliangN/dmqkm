from lib.api_template import ApiTemplate
from datas.read_yaml import Yamls

# 设置模块
class Settings:
    def __init__(self):
        self.datas = Yamls()

    # 成功-修改昵称
    def change_nick(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "nick": "大宝贝"}
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    # 失败-昵称已存在
    def nickExist(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "nick": "大宝贝1"}
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    # 失败-昵称敏感词
    def nickSensitiveWord(self, data):
        print(data)
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "nick": "操"}
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json

    # 失败-昵称为空
    def nickNull(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "nick": " "}
        res_json = ApiTemplate().post_api(path, data)
        print(res_json)
        return res_json


    # 成功-修改用户签名数字
    def changeSignature(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "introduction": "6666"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json

    # 成功 - 修改用户签名文字
    def changeSignatureletter(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "introduction": "来吧"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json

    # 成功 - 修改用户签名特殊符号
    def changeSignatureSymbol(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "introduction": "@#￥%……A&"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json

    # 失败-签名敏感字校验
    def changeSignaFail(self, data, datas):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": self.datas.read_yml()['public']['selfUserCode'],
                "deviceId": self.datas.read_yml()['public']['deviceId'],
                "sign": self.datas.read_yml()['public']['sign'],
                "introduction": datas}
        res_json = ApiTemplate().post_api(path,data)
        return res_json



if __name__ == '__main__':
    a =Settings()
    print(a.changeming())