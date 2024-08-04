from pymysql import Connection


def study_connection():

    # 创建连接对象
    conn = Connection(
            user="root",
            password="20001030",
            host="127.0.0.1",
            port=3306,
            database="mp"
            )
    print(conn.get_server_info())

    # 获取游标对象
    cursor = conn.cursor()

    # 通过游标对象执行SQL
    cursor.execute("select * from user")

    # 获取执行结果,并放到一个元祖中
    result: tuple = cursor.fetchall()

    for row in result:
        print(row)


    # 关闭连接
    conn.close()


if __name__ == '__main__':
    """
    掌握使用pymysql模块连接mysql，并操作数据
    """
    study_connection()

    pass