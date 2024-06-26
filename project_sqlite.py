try:
    import streamlit as st
except ImportError:
    import os
    os.system('pip install streamlit')
    import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from insert_sqlite import *
from update_sqlite import *
from delete_sqlite import *
from create_sqlitedb_from_file import *
from credentials import *
from create_sqlite_user import *


def format_list(list):
    list = [str(item) for item in list]
    new_list = '\n'.join(list)
    new_list = new_list.replace('[', '')
    new_list = new_list.replace(']', '')
    new_list = new_list.replace("'", "")
    new_list = new_list.replace('(', '')
    new_list = new_list.replace(')', '')
    new_list = new_list.replace(',', '')
    return new_list

projectdb = sqlite3.connect('project.db')
studentcursor = projectdb.cursor()


placeholder1 = st.empty()
placeholder = st.empty()
username = placeholder1.text_input('Enter your username: ', key='1')
password = placeholder.text_input('Enter your password: ', type='password', key='2')

# check credentials from the credentials.py file
# print(f'USERNAME: {credentials["admin"]["username"]}')

if (username == credentials["student"]["username"] and password == credentials["student"]["password"]) or (username == credentials["admin"]["username"] and password == credentials["admin"]["password"]):
    st.success('Login successful!')
    st.write('\n')
    # current_date = '2024-04-01'

    # The current date
    now = datetime.now()
    current_date = now.strftime("%Y-%m-%d")
    st.write('Current date:', current_date)

    # add a dropdown for the options
    if username == credentials["admin"]["username"] and password == credentials["admin"]["password"]:
        st.write("To reset the database, you must select the `Select An Option` choice first, then select `Reset Database`")
        username = 'Admin'
        user_check = user(studentcursor, projectdb)
        user_check.create_user(username)
        options = ['Select An Option','Reset Database', 'Add Project', 'Update Project', 'Delete Project']
        option = st.selectbox('Select an option', options)
    else:
        options = ['Select An Option', 'Add Project']
        option = st.selectbox('Select an option', options)
    # print(option)
        
    

    if option == 'Reset Database':
        reset = create(studentcursor, projectdb)
        reset.create_db()
        st.write('Database reset successful')

    elif option == 'Add Project':
        # print(f'USERS: {users}')
        st.write(f'`{username}` user active')
        # st.write(f"USER ID: {user_id}")

        project_name = st.text_input('Enter the project name: ')
        project_description = st.text_input('Enter the project description: ')
        confirm_insert = st.button('Insert data')
        if confirm_insert:
            insert_data = insert(studentcursor, projectdb)
            insert_data.insert_data(project_name, project_description, username, current_date)
            st.write('Data inserted successfully!')
    elif option == 'Update Project':
        # Check for users in the database
        try:
            # studentcursor.execute("USE project")
            studentcursor.execute("SELECT user_project_id FROM user_project WHERE user_project_id IS NOT NULL")
            users = studentcursor.fetchall()
        except sqlite3.Error as err:
            # st.write(f'Table does not exist: {err}')
            users = None

        if not users:
            st.write('No users with projects in the database')
        else:
            studentcursor.execute("""SELECT project_name
                                    ,      project_description
                                    ,      username
                                    ,      last_update_date
                                    FROM   project p
                                    INNER JOIN user_project up
                                    ON p.project_id = up.project_id
                                    INNER JOIN user u
                                    ON u.user_id = up.user_id
                                """)
            data = studentcursor.fetchall()
            # print(data)
            df = pd.DataFrame(data, columns=['Project Name', 'Project Description', 'Owner', 'Date Added'])
            st.write(df)

            project_name = st.text_input('Enter the project name to update: ')
            project_description = st.text_input('Enter the new project description: ')
            # ask the user if they need to update the name of the project
            update_name = st.checkbox('Update the project name?')

            if update_name:
                new_project_name = st.text_input('Enter the new project name: ')
                confirm_name_update = st.button('Update Project Name')
                if confirm_name_update:
                    new_project_name = new_project_name
            else:
                new_project_name = None

            confirm_update = st.button('Update data')
            if confirm_update:
                if project_description == '':
                    project_description = None
                update_data = update(studentcursor, projectdb)
                update_data.update_data(project_name, project_description, username, current_date, new_project_name)
                st.write('Data updated successfully!')

    elif option == 'Delete Project':
        # Check for users in the database
        try:
            # studentcursor.execute("USE project")
            studentcursor.execute("SELECT user_project_id FROM user_project WHERE user_project_id IS NOT NULL")
            users = studentcursor.fetchall()
        except sqlite3.Error as err:
            # st.write(f'Table does not exist: {err}')
            users = None

        if not users:
            st.write('No users with projects in the database')
        else:
            studentcursor.execute("""SELECT project_name
                                    ,      project_description
                                    ,      username
                                    ,      last_update_date
                                    FROM   project p
                                    INNER JOIN user_project up
                                    ON p.project_id = up.project_id
                                    INNER JOIN user u
                                    ON u.user_id = up.user_id
                                """)
            data = studentcursor.fetchall()
            # print(data)
            df = pd.DataFrame(data, columns=['Project Name', 'Project Description', 'Username', 'Date Added'])
            st.write(df)

            project_name = st.text_input('Enter the project name to delete: ')
            confirm_delete = st.button('Delete data')
            if confirm_delete:
                delete_data = delete(studentcursor, projectdb)
                delete_data.delete_data(project_name)
                st.write('Data deleted successfully!')


view = st.checkbox('View the data?')

if view:
    # Check for users in the database
    try:
        # studentcursor.execute("USE project")
        studentcursor.execute("SELECT user_project_id FROM user_project WHERE user_project_id IS NOT NULL")
        users = studentcursor.fetchall()
    except sqlite3.Error as err:
        # st.write(f'Table does not exist: {err}')
        users = None

    if not users:
        st.write('No users with projects in the database')
    else:
        studentcursor.execute("""SELECT project_name
                                ,      project_description
                                ,      u.username
                                ,      date_added
                                ,      u2.username
                                ,      last_update_date
                                FROM   project p
                                LEFT JOIN user_project up
                                ON p.project_id = up.project_id
                                LEFT JOIN user u
                                ON u.user_id = up.user_id
                                LEFT JOIN user u2
                                ON u2.user_id = up.last_updated_by
                            """)
        data = studentcursor.fetchall()
        # print(data)
        df = pd.DataFrame(data, columns=['Project Name', 'Project Description', 'Owner', 'Date Added', 'Last Updated By','Last Update Date'])
        st.write(df)