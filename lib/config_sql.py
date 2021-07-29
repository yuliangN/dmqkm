import pymysql
import logging


# 返回数据库连接
def get_db_conn():
    db_host = 'tx-bj-pt-uat-service01.reworldgame.com'
    db_port = 5809
    db_user = 'root'
    db_passwd = 'Em77QN4G#yPUpalnGH?'
    db = 'dmqk_account'
    conn = pymysql.connect(host=db_host,
                           port=db_port,
                           user=db_user,
                           passwd=db_passwd,
                           db=db
                           )
    return conn


class DB:

    # 改
    def change_db(sql):
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

    # # 删
    # def delete_db(sql):
    #     conn = get_db_conn()
    #     cur = conn.cursor()
    #     cur.execute(sql)
    #     conn.commit()

    # 查询
    def query_db(sql):
        logging.debug(sql)
        conn = get_db_conn()
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        logging.debug(result)
        return result

    # 查看游戏详情列表
    def check_mapid(mapid):
        sql = "select * from dmqk_game.g_map where map_id='%s'" % mapid
        return DB.query_db(sql)

    # 查询用户
    def check_mobile(mobile):
        sql = "select * from dmqk_account.t_account where mobile='%s'" % mobile
        return DB.query_db(sql)

    # 删除用户
    def del_mobile(mobile):
        sql = "DELETE from dmqk_account.t_account where mobile='%s'" % mobile
        return DB.change_db(sql)

# if __name__ == '__main__':
# print(check_mapid('1055'))
# print(DB.check_mobile(17611523112))
# print(DB.del_mobile(13911111045))
