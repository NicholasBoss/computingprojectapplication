# Database Setup

## Introduction

This week we are going to create the database we will use for our project. We will use MySQL Workbench as our database management tool. 

## Instructions

1. Run the setup.py script to create the user and grant permissions to the user.

2. Open MySQL Workbench, open a new ERD model and rename the database to `projectdb`.

3. Create the tables for the database.
    * There are 3 tables that will be created.
        * `user`
        * `project`
        * `user_project`

    * Each table will have a Primary Key and columns that will store the actual data we will put in.
    Primary Keys are unique identifiers for each row in the table. They are used to reference the row in other tables.
    We will use relationships to connect the tables together. These result in creating Foreign Keys in the tables. Foreign Keys are used to reference the Primary Key in another table.
    Primary keys are set to specific settings. In our project we will use the following settings:
        * INT data type
        * NOT NULL
        * UNSIGNED
        * AUTO_INCREMENT

4. Create the relationships between the tables.
    * The `user` table will have a one-to-many relationship with the `user_project` table.
    * The `project` table will have a one-to-many relationship with the `user_project` table.

    * We will manually create the relationships in MySQL Workbench. This is done within the `user_project` table. We will create a Foreign Key that references the Primary Key in the `user` table and the `project` table.

    * To create the foreign keys, we need to create the columns in the `user_project` table that will reference the Primary Keys in the `user` and `project` tables. The columns will be named `user_id` and `project_id`. They will be an INT data type with UNSIGNED and NOT NULL constraints. 

    * When the columns are created, we can create the Foreign Key constraints. Go to the `Foreign Keys` tab in the `user_project` table. Double-click under the Foreign Key Name column and name the constraint `user_project_fk1`. This will reference the user table. Click the checkbox next to user_id and it will assign the column to the primary key of the user table. Repeat this same process with the project table, but with the contraint named `user_project_fk2` and the project_id column.

5. Add some extra columns in the `user_project` table.
    * We will add three extra columns in the `user_project` table. These columns will be:
        * `date_added` - This will be a DATE data type that will store the date the project was added to the database.
        * `last_updated_by` - This will be a Foreign key reference to the `user` table. This will store the user_id of the user that last updated the project. This key will allow NULL values as the name and description may not have benn updated.
        * `last_updated_date` - This will be a DATE data type that will store the date the project was last updated.

6. Forward Engineer the database to make it useable.
    * Once the tables are created and the relationships are set, we can forward engineer the database to create the database in MySQL Workbench.

    * Go to the `Database` menu and select `Forward Engineer`. This will open a wizard that will guide you through the process of creating the database.

    * Select the connection you want to use and click `Next`.

    * There are two options we want to check at this point. The first is `DROP objects before each CREATE object`. This will drop the tables if they already exist. The second is `Generate DROP SCHEMA`. This will drop the schema (database) if it already exists. Click `Next`.

    * The next screen will ask you for the password to the user you chose at the beginning step. Enter the password and click `Next`.

    * The next screen will show you the SQL script that will be run to create the database. Click the `Save to file` option and save the file to your repository. Click `Next`.

    * The final screen will show you the progress of the script. Once it is finished, click `Finish`/`Close`.

    * You may also want to save the ERD model itself. Go to the `File` menu and select `Save Model`. Save the model to your repository.

7. Commit and push the changes to your repository.
    * Once the database is created, commit and push the changes to your repository. This will allow you to have a backup of the database in case you need to recreate it.

