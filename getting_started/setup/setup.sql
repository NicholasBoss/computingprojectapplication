-- ~
CREATE USER IF NOT EXISTS 'project_manager'@'localhost' IDENTIFIED BY 'manager';
-- ~
-- ~
GRANT ALL ON projectdb.* TO 'project_manager'@'localhost';
-- ~
