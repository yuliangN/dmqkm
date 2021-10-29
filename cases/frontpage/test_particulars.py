# -*- coding:utf-8 -*-
import allure
import pytest
from datas.read_yaml import users
from api.particulars_api import Particulars
from lib.config_sql import db


@allure.feature("详情页")
class TestParticulars:

    def setup_class(self):
        self.particulars = Particulars()

    @allure.story("查询游戏详情成功-输入上架的游戏id")
    @pytest.mark.parametrize('data', users.read_feedback()['mapid1'])
    def test_game_up(self, data):
        r = self.particulars.game_particulars(data)
        assert r.get('code') == 1
        assert r.get('data')['mapId'] == ''.join(list(map(str, data)))

    @allure.story("查询游戏详情成功-输入下架游戏id")
    @pytest.mark.parametrize('data', users.read_feedback()['mapid2'])
    def test_game_down(self, data):
        r = self.particulars.game_particulars(data)
        assert r.get('code') == 1
        assert r.get('data')['mapId'] == ''.join(list(map(str, data)))

    @allure.story("查询游戏详情失败-输入不存在的游戏id")
    @pytest.mark.parametrize('data', users.read_feedback()['mapid3'])
    def test_game_nonentity(self, data):
        r = self.particulars.game_particulars(data)
        assert r.get('code') == 1
        assert r.get('data') is None

    @allure.story("评论游戏成功-输入有效文字")
    @pytest.mark.parametrize('param1,param2', users.read_feedback()['mapid4'])
    def test_review(self, user, param1, param2):
        r = self.particulars.review_game(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("评论游戏成功-输入纯字母")
    @pytest.mark.parametrize('param1,param2', users.read_feedback()['mapid5'])
    def test_review_letter(self, user, param1, param2):
        r = self.particulars.review_game(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("评论游戏成功-输入纯数字")
    @pytest.mark.parametrize('param1,param2', users.read_feedback()['mapid6'])
    def test_review_number(self, user, param1, param2):
        r = self.particulars.review_game(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("评论游戏成功-输入有效的特殊字符")
    @pytest.mark.parametrize('param1,param2', users.read_feedback()['mapid7'])
    def test_review_special(self, user, param1, param2):
        r = self.particulars.review_game(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("评论游戏成功-输入有效的拼接字符")
    @pytest.mark.parametrize('param1,param2', users.read_feedback()['mapid8'])
    def test_review_joint(self, user, param1, param2):
        r = self.particulars.review_game(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("评论游戏失败-输入内容敏感字")
    @pytest.mark.parametrize('param1,param2', users.read_feedback()['mapid9'])
    def test_review_sensitivity(self, user, param1, param2):
        r = self.particulars.review_game(user, param1, param2)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("删除评论成功-输入正确的评论id")
    @pytest.mark.parametrize("param", users.read_feedback()['usercode'])
    def test_review_detele(self, user, param):
        r = self.particulars.review_delete(user, param)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    # @allure.story("评论回复成功-回复有效的从评论信息")
    # @pytest.mark.parametrize("param", users.read_feedback()['comment'])
    # def test_review_comment(self, user, param):
    #     r = self.particulars.review_comment(user, param)
    #     assert r.get('code') == 1
    #     assert r.get('message') == '操作成功'
