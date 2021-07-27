import requests

from api.login_api import Login


class TestLogin:

    def setup_class(self):
        self.login = Login()
        self.login.get_token()
        # print(self.login.get_token())

    def test_change_signature(self):
        r = requests.post("http://game.dreamreworld.com/api/acc/v1/profile/set",
                          data={"token": self.login.get_token(),
                                "selfUserCode":"27292686996733952",
                                "deviceId":"49500186-2b6d-60b6-2c40-add6f224ada4",
                                "sign":"daimaqian.sign",
                                "introduction": "qwe1231111333"})
        print(json.dumps(r.json(), indent=2, ensure_ascii=False))
        assert r.status_code == 200

