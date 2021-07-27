
from lib.api_template import ApiTemplate

# 设置页
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




    # # 修改用户签名
    # def changeSignature(self):
    #     r = requests.post("http://tx-bj-pt-uat-service01.reworldgame.com:8048/acc/v1/profile/set",
    #                       data={"token": "047922b5-80a9-40bc-aa1a-a1705d8c4732_09",
    #                             "selfUserCode": "27292686996733952",
    #                             "deviceId": "49500186-2b6d-60b6-2c40-add6f224ada4",
    #                             "sign": "daimaqian.sign",
    #                             "introduction": "3333"})
    #     return r

if __name__ == '__main__':
    a =Settings()
    print(a.changeming())