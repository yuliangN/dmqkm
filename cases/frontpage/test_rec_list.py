# -*- coding:utf-8 -*-
import allure
import pytest

from api.frontpage_api import FrontPage


@allure.feature("首页")
class TestRecList:

    def setup_class(self):
        self.frontpage = FrontPage()

    @allure.story("推荐列表查询成功")
    @pytest.mark.parametrize('data', [1, 2])  # data代码分页数
    def test_rec_list(self, data):
        r = self.frontpage.rec_map_list(data)
        assert r.get('code') == 1
        assert r.get('message') == '成功'

    @allure.story("新作列表查询成功")
    @pytest.mark.parametrize('data', [1, 2, 3, 4])  # data代码分页数
    def test_new_work(self, data):
        r = self.frontpage.new_work(data)
        assert r.get('code') == 1
        assert r.get('message') == '操作成功'
