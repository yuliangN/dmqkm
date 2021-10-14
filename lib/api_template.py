import requests
from lib.log_api import log
from datas.read_yaml import Yamls


class ApiTemplate:
    # 封装域名+端口
    def common(self,path):
        host = Yamls().read_yml()['env200']['host'] + ':' + str(Yamls().read_yml()['env200']['port'])
        url = host + str(path)
        return url

    # post请求
    def post_api(self, path, data, **files):
        log.info(f"接口请求入参为 ：{data}")
        url = self.common(path)
        res = requests.post(url=url, data=data, **files)
        res_json = res.json()
        return res_json

    # get请求
    def get_api(self, path, data):
        url = requests.common(path)
        res = requests.get(url=url, data=data)
        res_json = res.json()
        return res_json

