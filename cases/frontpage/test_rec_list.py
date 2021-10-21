# -*- coding:utf-8 -*-
import allure
import pytest
from datas.read_yaml import users
from api.frontpage_api import FrontPage


@allure.feature("首页")
class TestRecList:

    def setup_class(self):
        self.frontpage = FrontPage()

    @allure.story("推荐列表查询-成功")
    @pytest.mark.parametrize('data', [1, 2])  # data代码分页数
    def test_rec_list(self, data):
        r = self.frontpage.rec_map_list(data)
        assert r.get('code') == 1
        assert r.get('message') == '成功'

    @allure.story("新作列表查询-成功")
    @pytest.mark.parametrize('data', [1, 2, 3, 4])  # data代码分页数
    def test_new_work(self, data):
        r = self.frontpage.new_work(data)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("搜索热门推荐、历史记录-成功")
    def test_new_work(self):
        r = self.frontpage.search()
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'

    @allure.story("搜索游戏-成功")
    @pytest.mark.parametrize("param", users.read_feedback()['data5'])
    def test_game_search(self, param):
        r = self.frontpage.game_search(param)
        assert r.get('code') == 1
        assert int(r.get('data')['total']) >= 1

    @allure.story("搜索游戏-游戏名为空搜索")
    @pytest.mark.parametrize("param", users.read_feedback()['data6'])
    def test_game_null(self, param):
        r = self.frontpage.game_search(param)
        assert r.get('code') == 1
        assert int(r.get('data')['total']) == 0

    @allure.story("搜索游戏-输入的内容没有查找到游戏")
    @pytest.mark.parametrize("param", users.read_feedback()['data7'])
    def test_game_notfound(self, param):
        r = self.frontpage.game_search(param)
        assert r.get('code') == 1
        assert int(r.get('data')['total']) == 0
