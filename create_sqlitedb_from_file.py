import mysql.connector
import sqlite3
class create:

    def __init__(self, db_cursor, db_connection):
        self.db_cursor = db_cursor
        self.db_connection = db_connection
        
    def create_db(self):
        # rollback the database if an error occurs
        try:
            drop_count = 0
            create_count = 0
            number = 0
            edit_file = open('project_sqlite.sql', 'r+')
            file_contents = edit_file.read()

            if not file_contents.__contains__('-- ~'):
                print('Formatting File...')
                file_contents = file_contents.replace("DROP", "-- ~\nDROP")
                file_contents = file_contents.replace("CREATE", "-- ~\nCREATE")
                file_contents = file_contents.replace(";", ";\n-- ~")
                edit_file.seek(0)
                edit_file.write(file_contents)
                edit_file.truncate()
                edit_file.close()
            else:
                edit_file.close()
                print('File already formatted')

            f = open('project_sqlite.sql', 'r')
            sql_script = f.read()
            sql_commands = sql_script.split('-- ~')

            sql_commands = [command.strip() for command in sql_commands]

            for command in sql_commands:
                if command.lower().__contains__('drop table'):
                    drop_count += 1
                    number += 1
                if command.lower().__contains__('create table'):
                    create_count += 1
                    number += 1
                try:
                    self.db_cursor.execute(command)
                except sqlite3.Error as err:
                    print("Error Found")
                    print("----------ERROR DETAILS----------")
                    print(f'Query {number}. Error: {err}')
                    print('-------QUERY-------')
                    print(f'{command}\n')

                    self.db_connection.rollback()
                
            self.db_connection.commit()
            print(f'{drop_count} tables dropped')
            print(f'{create_count} tables created')
            f.close()
        except sqlite3.Error as err:
            print("Error Found")
            print("----------ERROR DETAILS----------")
            print(f'Query {number}. Error: {err}')
            print('-------QUERY-------')
            print(f'{command}\n')

            self.db_connection.rollback()