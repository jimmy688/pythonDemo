import pymysql
import random

class MysqlDemo:
    def __init__(self):
        pass

    def get_conn(self):
        conn=pymysql.connect(
            host="192.168.239.137",
            port=3306,
            user="root",
            password="krystal",
            db="pymysql",
            charset="utf8"
        )
        return conn


if __name__=='__main__':
    #获取cursor游标
    conn=MysqlDemo().get_conn()
    cursor=conn.cursor()

    #插入数据：
    sql1='insert into `users`(id,name) values(1,"jimmy"),(2,"krystal")'
    cursor.execute(sql1)

    #插入多条数据：
    sql2='insert into `users`(id,name) values(%s,%s)'
    sql2_data=[]

    for i in range(3,10):
        name="".join(random.sample('asdfghjklzxcvbnmqwertuyiop',5))
        id=i
        sql2_data.append((i,name))  # 封装为元组，并追加到列表中
        print(sql2_data)
    cursor.executemany(sql2,sql2_data)

    #查询数据
    sql3='select * from users limit 3'
    cursor.execute(sql3)
    data1=cursor.fetchone()  #获取一条数据,为元组类型
    data2=cursor.fetchall()  #获取所有数据，为元组类型，元组包含元组

    print("name:{},id:{}".format(data1[0],data1[1]))

    for row in data2:
        name=row[0]
        id=row[1]
        print("name:{},id:{}".format(name, id))

    #删除数据
    sql4='delete from users where id=1'
    try:
        cursor.execute(sql4)
    except Exception:
        print("删除失败")

    conn.commit()
    cursor.close()
    conn.close()





