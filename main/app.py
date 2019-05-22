import os

import psycopg2


class DataBase:

    def __init__(self, host, port, dbname, user, password):
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def __str__(self):
        return f'{self.host} - {self.port} - {self.dbname} - {self.user} - {self.password}'

    def fill_test_data(self):
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        cur = conn.cursor()
        # cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")
        cur.execute("CREATE TABLE IF NOT EXISTS phone_numbers (id serial PRIMARY KEY, number varchar);")
        # cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abcdef"))
        cur.execute("INSERT INTO phone_numbers (number) VALUES (%s)", ("3809712332144",))
        cur.execute("INSERT INTO phone_numbers (number) VALUES (%s)", ("3809743232144",))
        cur.execute("INSERT INTO phone_numbers (number) VALUES (%s)", ("3809765465788",))
        cur.execute("INSERT INTO phone_numbers (number) VALUES (%s)", ("3806576777274",))
        cur.execute("INSERT INTO phone_numbers (number) VALUES (%s)", ("3809445435345",))
        # cur.execute("SELECT * FROM test;")
        # result = cur.fetchone()
        # print(result)
        conn.commit()
        cur.close()
        conn.close()

    def find_number(self, number):
        conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM phone_numbers WHERE number LIKE '{number}%' LIMIT 10")
        result = cur.fetchall()
        # print(result)
        cur.close()
        conn.close()
        return result

    # def connect(self):
    #     conn = psycopg2.connect()


class Application:

    def __init__(self, database):
        self.database = database

    def run(self):
        while True:
            # TODO: Blank line
            input_ = input('Enter number: ')
            if input_ == 'q':
                return
            numbers = self.database.find_number(input_)
            print([int(number[1]) for number in numbers])
            # print([number for number in numbers])

    def stop(self):
        pass

    # host=os.environ.get('DB_HOST'),
    # port=os.environ.get('DB_PORT'),
    # dbname=os.environ.get('DB_NAME'),
    # user=os.environ.get('DB_USER')


database = DataBase(host='127.0.0.1', port=5433, dbname='phones', user='phones_user', password='phones')
application = Application(database=database)


if __name__ == '__main__':
    application.run()
    # print(database)
    # print(database.dbname)
    # print(database.host)
    # database.fill_test_data()
    # database.find_number('38097')
