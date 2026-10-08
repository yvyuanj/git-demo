import pymysql

# ==========1.新增数据==========
def add_user():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="Root@123456",
        charset='utf8',
        database='unicom'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into admin(username,password,mobile) values(%s,%s,%s)"
    cursor.execute(sql, ["wupeiqi", "qwe123", "15155555555"])
    conn.commit()
    print("新增成功")
    cursor.close()
    conn.close()

# ==========2.查询数据==========
def query_user():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="Root@123456",
        charset='utf8',
        database='unicom'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor.execute("select * from admin")
    data_list = cursor.fetchall()
    print("查询结果：")
    for row in data_list:
        print(row)
    cursor.close()
    conn.close()
# ==========3.修改数据==========
def update_user():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="Root@123456",
        charset='utf8',
        database='unicom'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 修改id=2这条的手机号
    sql = "update admin set mobile=%s where id=%s"
    cursor.execute(sql, ["13800138000", 2])
    conn.commit()
    print("修改成功")
    cursor.close()
    conn.close()

# ==========4.删除数据==========
def delete_user():
    conn = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user='root',
        password="Root@123456",
        charset='utf8',
        database='unicom'
    )
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "delete from admin where id=%s"
    cursor.execute(sql, [2])
    conn.commit()
    print("删除成功")
    cursor.close()
    conn.close()

if __name__ == '__main__':
    # add_user()       # 注释，不要再新增数据
    print("===== 修改前 =====")
    query_user()
    update_user()
    print("===== 修改后 =====")
    query_user()
    delete_user()
    print("===== 删除后 =====")
    query_user()

