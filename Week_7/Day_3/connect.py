import psycopg2
#
# conn = psycopg2.connect(host = 'localhost', database= 'bookstore', user = 'postgres', password='herpderp')
# cur = conn.cursor()
# sql = 'SELECT * FROM Book LIMIT 10'
#
# cur.execute(sql)
# results = cur.fetchall()
#
# print(results)


class SqlMagic():
    def __init__(self):
        self.connect()

    def connect(self):
        conn = psycopg2.connect(host='localhost', database='bookstore', user='postgres', password='herpderp')
        self.cur = conn.cursor()
        return True

    def execute(self, sql):
        self.cur.execute(sql)
        results = self.cur.fetchall()
        return results

    def all(self):
        sql ='SELECT * FROM Book LIMIT 10'
        return self.execute(sql)
