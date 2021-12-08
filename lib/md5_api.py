import hashlib


class Md5Api:
    # 密码md5加密
    def get_password(self, pwd):
        public_key = 'LbQzXNFiXEW5efM3'
        password = pwd + public_key
        md5 = hashlib.md5()
        md5.update(password.encode(encoding='utf-8'))
        print(md5.hexdigest().lower())
        return md5.hexdigest().lower()
