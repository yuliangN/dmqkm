
import yaml
import os


class Yamls:
    # 获取配置域名+端口号
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

    # 正确的账号和密码
    def read_user(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
        config_path = os.path.join(base_path, 'user.yaml')
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f.read())
        return data

    # def read_user_fail(self):
    #     base_path = os.path.dirname(os.path.realpath(__file__))
    #     # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
    #     config_path = os.path.join(base_path, 'user.yaml')
    #     with open(config_path, 'r', encoding='utf-8') as f:
    #         data = yaml.safe_load(f.read())
    #     return data

    # 获取反馈与建议信息
    def read_feedback(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
        config_path = os.path.join(base_path, 'couple.yaml')
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f.read())
        return data

    # 获取个人资料
    def read_personal(self):
        base_path = os.path.dirname(os.path.realpath(__file__))
        # 获取当前配置文件的路径，相当于根路径，读取config.yaml配置文件
        config_path = os.path.join(base_path, 'personal')
        with open(config_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f.read())
        return data


users = Yamls()
# if __name__ == '__main__':
