# -*- coding:utf-8 -*-
from datas.read_yaml import users
from lib.api_template import ApiTemplate
from lib.config_sql import db
from lib.log_api import log


# 游戏详情模块
class Particulars:

    # 查询详情页
    def game_particulars(self, data):
        path = '/game/v1/mapInfo'
        data = {"mapId": data,
                'deviceId': users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "sign": users.read_yml()['public']['sign']}
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 评论游戏
    def review_game(self, data, param1, param2):
        path = '/review/game/insert'
        data = {"token": data,
                'deviceId': users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "sign": users.read_yml()['public']['sign'],
                "osType": users.read_yml()['public']['osType'],
                "mapId": param1,
                "content": param2
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 删除评论
    def review_delete(self, token, param):
        id = db.review_first(''.join(list(map(str, param))))
        path = '/review/game/remove'
        data = {"token": token,
                'deviceId': users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "sign": users.read_yml()['public']['sign'],
                "osType": users.read_yml()['public']['osType'],
                "id": id
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 回复评论
    def review_comment(self, token, param1):
        usercode = " ".join(map(str, users.read_feedback()['usercode']))
        # 获取用户的id和评论的父id
        map_list = db.review_id(usercode[1:-1])
        if map_list[0][0] == 0:
            parentId = map_list[0][1]
        else:
            parentId = map_list[0][0]
        path = '/review/game/insert'
        data = {"token": token,
                'deviceId': users.read_yml()['public']['deviceId'],
                "lang": users.read_yml()['public']['lang'],
                "sign": users.read_yml()['public']['sign'],
                "osType": users.read_yml()['public']['osType'],
                "mapId": map_list[0][2],
                "parentId": parentId,
                "content": param1
                }
        res_json = ApiTemplate().post_api(path, data)
        log.info(f"接口返回结果为 ：{res_json}")
        return res_json

    # 删除回复

    # 举报评论

    # 举报游戏

    # 喜欢游戏

    # 投票

    # 房间

    # 分享
