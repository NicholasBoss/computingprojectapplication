class insert:
    def __init__(self, cursor, conn):
        self.cursor = cursor
        self.conn = conn

    def insert_data(self, project_name, project_description, username, current_date):
        self.cursor.execute("""INSERT INTO project 
                            (project_name, project_description) 
                            VALUES 
                            (?, ?)""", 
                            (project_name, project_description))
        self.conn.commit()
        project_id = self.cursor.lastrowid
        # print(f"PROJECT ID: {project_id}")
        user_id = self.cursor.execute("""SELECT user_id 
                                      FROM user 
                                      WHERE username = ?""", (username,))
        user_id = self.cursor.fetchone()
        user_id = user_id[0]
        # print(f"USER ID: {user_id}")
        self.cursor.execute("""INSERT INTO user_project 
                            (user_id, project_id, date_added, last_updated_by, last_update_date) 
                            VALUES 
                            (?, ?, ?, ?, ?)""", 
                            (user_id, project_id, current_date, user_id, current_date))
        self.conn.commit()
