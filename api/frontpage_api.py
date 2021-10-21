# -*- coding:utf-8 -*-
from lib.api_template import ApiTemplate
from lib.log_api import log
from datas.read_yaml import users


# 首页模块
class FrontPage:

    # 推荐
    def rec_map_list(self, data):
        path = '/webop/app/v1/rank/map/list'
        data = {
            "selfUserCode": users.read_yml()['public']['selfUserCode'],
            "deviceId": users.read_yml()['public']['deviceId'],
            "sign": users.read_yml()['public']['sign'],
            "lang": users.read_yml()['public']['lang'],
            "adId": users.read_yml()['public']['adId'],
            "pageId": data,
            "pageSize": 20,
            "rankId": 3
        }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 新作
    def new_work(self, data):
        path = '/game/app/v1/findMapList'
        data = {
            "selfUserCode": users.read_yml()['public']['selfUserCode'],
            "deviceId": users.read_yml()['public']['deviceId'],
            "sign": users.read_yml()['public']['sign'],
            "lang": users.read_yml()['public']['lang'],
            "adId": users.read_yml()['public']['adId'],
            "pageId": data,
            "pageSize": 20,
            "rankId": 4
        }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 搜索历史与推荐游戏
    def search(self):
        path = '/game/v1/searchword'
        data = {
            "deviceId": users.read_yml()['public']['deviceId'],
            "sign": users.read_yml()['public']['sign'],
            "lang": users.read_yml()['public']['lang'],
            "adId": users.read_yml()['public']['adId'],
        }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 搜索游戏
    def game_search(self, param):
        path = '/game/v1/search'
        data = {
            "deviceId": users.read_yml()['public']['deviceId'],
            "sign": users.read_yml()['public']['sign'],
            "lang": users.read_yml()['public']['lang'],
            "adId": users.read_yml()['public']['adId'],
            "keyword": param,
            "pageId": 1,
            "pageSize": 20,
        }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json
