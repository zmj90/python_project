import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster01@python.org', 'very-secret01'))
        # ins = 'insert into filmtab values(%s,%s,%s)'
        # cursor.execute(ins, ['霸王别姬', '张国荣', '1993'])

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email` like %s"
        cursor.execute(sql, ('%webmaster%',))
        result = cursor.fetchone()
        # result = cursor.fetchmany(2)
        # result = cursor.fetchall()
        print(result, type(result))
