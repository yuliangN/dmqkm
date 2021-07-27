import yaml
import json
import os

def read_yml():
    """
    获取当前环境的绝对路径
    :return:
    """
    base_path = os.path.dirname(os.path.realpath(__file__))
    # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
    config_path = os.path.join(base_path,'config.yaml')
    with open(config_path, 'r',encoding='utf-8') as f:
        data = yaml.safe_load(f.read())
    return data


# if __name__ == '__main__':
#     # print(read_yml()['env200']['host'])
#     # print(read_yml()['env200']['port'])
#     # read_yml()
#     url = read_yml()['env200']['host'] + ':'+json.dumps(read_yml()['env200']['port'])
#     print(url)
#     print(type(url))