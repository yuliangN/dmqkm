import json

import requests
class BaseApi:
    # 请求协议，
    def request(self,request:dict):
        if 'url' in request:
            return self.http_request(request)
        if 'rpc' == request.get("protocol"):
            return self.rpc_request(request)

    # http 请求
    def http_request(self,request):
        r = requests.request(**request)
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def _post(self,path,data=None):
        self.send('POST',self._host+':'+self._port+path,data=data)