import pymysql
from DBUtils.PooledDB import PooledDB
# from dbutils.pooled_db import PooledDB

class MySQL:
    host = '8.140.105.168'
    user = 'root'
    port = 3306
    pasword = 'songtao0404'
    db = 'Spider'
    charset = 'utf8'

    pool = None
    limit_count = 3  # 最低预启动数据库连接数量

    def __init__(self):
        self.pool = PooledDB(pymysql, self.limit_count, host=self.host, user=self.user, passwd=self.pasword, db=self.db,
                             port=self.port, charset=self.charset, use_unicode=True)

    def select(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def insert(self, sql):
        conn = self.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            conn.commit()
            return {'result': True, 'id': int(cursor.lastrowid)}
        except Exception as err:
            conn.rollback()
            return {'result': False, 'err': err}
        finally:
            cursor.close()
            conn.close()
    def insertMany(self,sql,datas):
        conn = self.pool.connection()
        cursor = conn.cursor()
        try:
            cursor.executemany(sql,datas)
            conn.commit()
            return {'result': True, 'id': int(cursor.lastrowid)}
        except Exception as err:
            conn.rollback()
            return{'result':False,'err':err}

