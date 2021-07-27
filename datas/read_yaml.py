import yaml
import os


class Yamls:
    def read_yml(self):
        """
        获取当前环境的绝对路径
        :return:
        """
        base_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
        config_path = os.path.join(base_path, 'config.yaml')
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f.read())
        return data

    def read_user(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
        config_path = os.path.join(base_path, 'user.yaml')
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f.read())
        return data


if __name__ == '__main__':
#     # print(read_yml()['env200']['host'])

print(Yamls().read_user())
# print(Yamls().read_user())
#     url = read_yml()['env200']['host'] + ':'+json.dumps(read_yml()['env200']['port'])
#     print(url)
#     print(type(url))