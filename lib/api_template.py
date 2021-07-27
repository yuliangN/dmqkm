import json
import requests

from datas.read_yaml import Yamls


class ApiTemplate:
    # 封装域名+端口
    Yamls
    def common(self,path):
        host = Yamls().read_yml()['env200']['host'] + ':' + str(Yamls().read_yml()['env200']['port'])
        url = host + str(path)
        return url

    # post请求
    def post_api(self,path,data):
        url = ApiTemplate().common(path)
        res = requests.post(url=url,data=data)
        res_json = res.json()
        return res_json

    # get请求
    def get_api(self, path,data):
        url = ApiTemplate().common(path)
        res = requests.get(url=url, data=data)
        res_json = res.json()
        return res_json

if __name__ == '__main__':
    pass
    # path = '/acc/v1/profile/set'
    # data = {"token": "047922b5-80a9-40bc-aa1a-a1705d8c4732_09",
    #         "selfUserCode": "27292686996733952",
    #         "deviceId": "49500186-2b6d-60b6-2c40-add6f224ada4",
    #         "sign": "daimaqian.sign",
    #         "introduction": "sdfdsfds33fd"}
    # res_json = ApiTemplate().post_api(path, data)
    # print(res_json)
    # a = ApiTemplate()
    # print(a.post_api('/aaa/vvv/bbb','{a:1.b:2}'))