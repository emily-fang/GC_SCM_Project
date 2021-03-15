#!/usr/bin/python

import psycopg2
class DataBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database="scm", user="db_admin", password="db_admin@2019",host="pgm-uf6zise6412hc6obno.pg.rds.aliyuncs.com", port="1433")
        except Exception as e:
            print(e)
    def database_close(self):
            self.conn.close()
#查询的sql语句
    def select_sql(self,sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            result=cur.fetchmany(2)
            return result
        except Exception as e:
            raise  e
            print("查询失败了")
            self.cur.close()
#增删改sql语句
    def select_update(self,sql):
        try:
            cur = self.conn.cursor()
            cur.execute(sql)
            cur.execute('commit')
            # cur.commit()
        except Exception as e:
            print("查询失败了，原因是",e)
if __name__ == '__main__':
    # sql="SELECT * FROM wip.wip_data WHERE  raw_version ='EHSB'"
    # result = DataBase().select_sql(sql)
    sql = "DELETE  FROM wip.wip_data WHERE  raw_version in('ADBB','EOEB','KOGB','EODB','IAQB','KOHB')"
    result = DataBase().select_update(sql)
    DataBase().database_close()

    # # sql = "SELECT * FROM wip.wip_data WHERE  raw_version in('ADBB','EOEB','KOGB','EODB','IAQB','KOHB')"
    # result =  DataBase().select_sql(sql)
    print(result)

