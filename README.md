# Overview

This project shows how to combine the languages of Python and SQL to create a simple database. The database can be created using either MySQL or SQLite. The Streamlit library allows the application to be used on the web. There are three "users" implemented: no user, a student user, and an admin user. 

The "no user" can only view the projects from the database. The "student user" can view the projects and add a project to the database. The "admin user" can view the projects, add, update, or delete a project, and even reset the database entirely.

# Installation

To use this project, you will need to install the following libraries:

```bash
pip install streamlit
pip install mysql-connector-python
```

# Usage

You will have two options to run the project. The first option is to use SQLite:

```bash
streamlit run project_sqlite.py
```

The second option is to use MySQL:

```bash
streamlit run project_mysql.py
```

If you choose to use MySQL, you will need to create a database and a user. 

# Database Setup

If you are on a local machine, you will need to install MySQL Workbench and MySQL Server. You can download MySQL Workbench [here](https://dev.mysql.com/downloads/workbench/). You can download MySQL Server [here](https://dev.mysql.com/downloads/mysql/).  

If you are on the AWS Instance the school provides, you just need to run the `setup.py` script in the `getting_started` folder.

 The `setup.py` script in the `getting_started` folder will create the database and user for you. You may need to edit the script at line 9 to include your own password.
