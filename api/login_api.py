from api.base_api import BaseApi
import requests
import json

class Login(BaseApi):

    def get_token(self):
        r = requests.post("http://tx-bj-pt-uat-service01.reworldgame.com:8048/acc/v1/login/password",
                          data={
                              "accountName": "13911112028",
                              "password": "qwe123",
                              "sign": "daimaqiankun.sign",
                              "deviceId": "15615615616",
                              "osType": "09",
                              "adId": 8001
                          })
        # print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return  r.json()['token']
