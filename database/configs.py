import operators

class database_configs():
    def __init__(self) -> None:
        self.dbName = 'database/db_main.db'
        self.make_conn()
        self.sql_create_table_universities = """ CREATE TABLE IF NOT EXISTS universities (
                                        name text NOT NULL,
                                        country text NOT NULL,
                                        rank integer,
                                        id integer primary key
                                    ); """
        self.sql_create_table_supervisors = """ CREATE TABLE IF NOT EXISTS supervisors (
                                        name text NOT NULL,
                                        university text NOT NULL,
                                        email text NOT NULL,
                                        country text NOT NULL,
                                        emailed text NOT NULL,
                                        answer text NOT NULL,
                                        interview text NOT NULL,
                                        position_type text NOT NULL,
                                        webpage text,
                                        university_rank integer,
                                        notes text,
                                        id integer primary key
                                    ); """
    def make_conn(self):
        self.conn = operators.create_connection(self.dbName)