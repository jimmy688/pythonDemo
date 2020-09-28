import pymysql

class MysqlUtils():
    def __init__(self):
        pass
    def get_conn(self):
        conn=pymysql.connect(
            host="192.168.239.137",
            port=3306,
            user="root",
            password="krystal",
            db="recruit_students",
            charset="utf8"
        )
        return conn
    def get_cursor(self):
        return self.get_conn().cursor()


    def get_data(self,sql):
        cursor=self.get_cursor()
        sql=sql
        cursor.execute(sql)
        data=cursor.fetchone()
        return data


if __name__=='__main__':
    mu=MysqlUtils()
    data=mu.get_data('SELECT f_school_id FROM `t_login_account` ' \
            'order by f_school_id desc limit 1;')
    print(data[0])
