import mysql.connector
class user:

    def __init__(self, studentcursor, projectdb):
        self.studentcursor = studentcursor
        self.projectdb = projectdb

    def format_list(self, list):
        list = [str(item) for item in list]
        new_list = '\n'.join(list)
        new_list = new_list.replace('[', '')
        new_list = new_list.replace(']', '')
        new_list = new_list.replace("'", "")
        new_list = new_list.replace('(', '')
        new_list = new_list.replace(')', '')
        new_list = new_list.replace(',', '')
        return new_list

    def create_user(self, username):
        try:
            self.studentcursor.execute("USE projectdb")
            # Check to see if user exists in the database
            self.studentcursor.execute("SELECT username FROM user")
            users = self.studentcursor.fetchall()
            users = self.format_list(users)
            if username in users:
                # close the cursor
                self.studentcursor.close()
                return True, username
            # Insert the user into the database if they are not already there
            else:
                self.studentcursor.execute("INSERT INTO user (username) VALUES (%s)", (username,))
                self.projectdb.commit()
                print('User inserted successfully')
                return True, username
        except mysql.connector.Error as err:
            print(f'Error: {err}')
            return False