class insert:
    def __init__(self, studentcursor, projectdb):
        self.studentcursor = studentcursor
        self.projectdb = projectdb

    def insert_data(self, project_name, project_description, username, current_date):
        self.studentcursor.execute("""INSERT INTO project 
                            (project_name, project_description) 
                            VALUES 
                            (?, ?)""", 
                            (project_name, project_description))
        self.projectdb.commit()
        project_id = self.studentcursor.lastrowid
        # print(f"PROJECT ID: {project_id}")
        user_id = self.studentcursor.execute("""SELECT user_id 
                                             FROM user 
                                             WHERE username = ?""", (username,))
        user_id = self.studentcursor.fetchone()
        user_id = user_id[0]
        # print(f"USER ID: {user_id}")
        self.studentcursor.execute("""INSERT INTO user_project 
                            (user_id, project_id, date_added, last_updated_by, last_update_date) 
                            VALUES 
                            (?, ?, ?, ?, ?)""", 
                            (user_id, project_id, current_date, user_id, current_date))
        self.projectdb.commit()
