# -*- coding=utf-8 -*-
import pytest
import random  # 导入随机模块


# 初始化，获取随机电话号
@pytest.fixture(scope='class')
def phone():
    phone_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                  "153", "155", "156", "157", "158", "159", "186", "187", "188", "173", "177", "180", "181", "189",
                  "199"]
    # 创建一个正确的手机前三位列表
    random_phone = random.choice(phone_list) + "".join(random.choice("0123456789") for i in range(8))
    """
    随机选取前三位，之后字符串拼接，随机选取数字循环8次r
    """
    return str(random_phone)
