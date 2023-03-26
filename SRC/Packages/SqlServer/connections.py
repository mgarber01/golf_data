import pyodbc


class Connection:
    def __init__(self, server, database, driver, user=None, pw=None, trusted=True):
        self.server = server
        self.database = database
        self.driver = driver
        self. user = user
        self.pw = pw
        self.trusted = trusted
        self.connection_string = self.connection_string()

    def conn_string(self):
        if self.trusted:
            return f'Driver={self.driver};\
            SERVER={self.server};\
            DATABASE={self.database};\
            Trusted_Connection = yes'
        elif self.user and self.pw:
            return f'Driver={self.driver};\
            SERVER={self.server};\
            DATABASE={self.database};UID={self.user};PWD={self.pw}'
        else:
            raise NotImplementedError

    def tables(self):
        pass
