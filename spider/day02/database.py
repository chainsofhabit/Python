import pymysql

def main():
    host = '127.0.0.1'
    port = 3306
    username = 'root'
    password = '123456'
    database = 'spider'
    db = pymysql.connect(host,username,password,database,charset='utf8',port=port)
    cursor = db.cursor()
    print(cursor)

    sql = "insert into test2 (title) values ('%s')" % 'carmack'
    cursor.execute(sql)
    db.commit()

if __name__ == '__main__':
    main()