import mysql.connector
import os
import platform

# connect to root user
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="C4nGet1n!",
)

# print(mydb)


# execute the root commands to grant access to the new user
directory = os.getcwd()
# check to see what system I'm using
name = platform.system()
if name == 'Linux' or name == 'Darwin':
    print("Linux/MacOS Detected")
    filename = f"{directory}/setup.sql"
elif name == 'Windows':
    print("Windows OS Detected")
    filename = f"{directory}\\setup.sql"

with open(filename, 'r+') as file:
    sqlFile = file.read()
    commands = sqlFile.split('-- ~')
    commands = [command.strip() for command in commands]
    for command in commands:
        # print(command)

        try:
            mycursor = mydb.cursor()
            mycursor.execute(command)
            mydb.commit()
        except Exception as e:
            print(e)
            continue

# close the connection
mydb.close()

# connect to the new user
manager = mysql.connector.connect(
    host="localhost",
    user="project_manager",
    password="manager",
)

managercursor = manager.cursor()
managercursor.execute("SHOW DATABASES")
output = managercursor.fetchall()
# print the databases
count = 0
for x in output:
    count += 1
    print(x)

print(f"{count} databases found")