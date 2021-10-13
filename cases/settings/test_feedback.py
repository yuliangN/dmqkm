import allure
import pytest
from datas.read_yaml import users

from api.setting_api import Settings


@allure.feature("反馈与建议")
class TestFeedback:

    def setup_class(self):
        self.settings = Settings()

    @allure.story("反馈成功-纯文本提交反馈数据")
    @pytest.mark.parametrize('param1,param2,param3', users.read_feedback()['data'])
    def test_feedback_text(self, user, param1, param2, param3):
        r = self.settings.feedback_text(user, param1, param2, param3)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("反馈成功-上传反馈图片")
    @pytest.mark.parametrize('param1,param2,param3', users.read_feedback()['data'])
    def test_feedback_image(self, user, param1, param2, param3):
        r = self.settings.feedback_image(user, param1, param2, param3)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    def test(self):
        print(users.read_feedback()['data'])
