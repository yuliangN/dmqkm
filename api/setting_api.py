
from lib.api_template import ApiTemplate


# 设置模块
class Settings():
    # 成功-修改用户签名数字
    def changeSignature(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": "27302859291230208",
                "deviceId": "49500186-2b6d-60b6-2c40-add6f224ada4",
                "sign": "daimaqian.sign",
                "introduction": "6666"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json

    # 成功 - 修改用户签名文字
    def changeSignatureletter(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": "27302859291230208",
                "deviceId": "49500186-2b6d-60b6-2c40-add6f224ada4",
                "sign": "daimaqian.sign",
                "introduction": "来吧"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json

    # 成功 - 修改用户签名特殊符号
    def changeSignatureSymbol(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": "27302859291230208",
                "deviceId": "49500186-2b6d-60b6-2c40-add6f224ada4",
                "sign": "daimaqian.sign",
                "introduction": "@#￥%……A&"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json

    # 失败-签名敏感字校验
    def changeSignaFail(self, data):
        path = '/acc/v1/profile/set'
        data = {"token": data,
                "selfUserCode": "27302859291230208",
                "deviceId": "49500186-2b6d-60b6-2c40-add6f224ada4",
                "sign": "daimaqian.sign",
                "introduction": "操"}
        res_json = ApiTemplate().post_api(path,data)
        return res_json


a

if __name__ == '__main__':
    a =Settings()
    print(a.changeming())