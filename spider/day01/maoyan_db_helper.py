import pymysql


#获取数据库连接
def get_db_connection():
    host = '127.0.0.1'
    port = 3306
    username = 'root'
    password = '123456'
    database = 'maoyan_db'
    db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
    return db

#获取数据库游标
def get_cursor(db):
    cursor = db.cursor()
    return cursor

#关闭数据库连接
def close_connection(db):
    db.close()

#插入一条数据,item为字典
def insert_record(db,cursor,item):
    sql = "insert into maoyan (actor,movie,rate,releasetime,score,cover) " \
          "values ('%s','%s','%s','%s','%s','%s')" % \
          (item['actor'],item['movie'],item['rate'],item['release'],item['score'],item['cover'])
    print(sql)
    cursor.execute(sql)

    db.commit()

