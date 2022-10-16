import pymysql


class MySQL:
    def __init__(self):
        self.__kwargs = {
            'user': 'root',
            'passwd': 'cl2016',
            'db': 'zm',
            'port': 3309,
            'host': 'localhost'
        }

    def __enter__(self):
        self.__db = pymysql.connect(**self.__kwargs)
        self.__cursor = self.__db.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__db.close()

    def get(self, sql: str):
        try:
            self.__cursor.execute(sql)
            return self.__cursor.fetchall()
        except Exception as e:
            print(e)
            print(f'SQL ERROR: \n{sql}\n')
            raise

    def row(self, sql: str):
        result = self.get(sql)
        if result:
            return self.get(sql)[0]

    def val(self, sql: str):
        return self.get(sql)[0][0]

    def col(self, sql: str):
        return [r[0] for r in self.get(sql)]

    def set(self, sql: str, show_sql=True):
        try:
            self.__cursor.execute(sql)
            self.__db.commit()
        except Exception as e:
            print(e)
            if show_sql:
                print(f'SQL ERROR: \n{sql}\n')
            raise

    @property
    def tables(self):
        return self.col(f'SHOW TABLES')

    def count(self, table, **args):
        if args:
            where = ''
            for key, value in args.items():
                if where:
                    where += ' AND'
                where += f' {key}="{value}"'
            count = self.val(f'SELECT COUNT(*) FROM `{table}` WHERE{where}')
        else:
            count = self.val(f'SELECT COUNT(*) FROM `{table}`')
        return int(count) if count else 0
