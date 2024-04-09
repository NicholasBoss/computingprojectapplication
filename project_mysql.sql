-- MySQL DB Creation Script

-- ~
DROP TABLE IF EXISTS `projectdb`.`user_project` ;
-- ~
-- ~
DROP TABLE IF EXISTS `projectdb`.`user` ;
-- ~
-- ~
DROP TABLE IF EXISTS `projectdb`.`project` ;
-- ~
-- -----------------------------------------------------
-- Table `projectdb`.`user`
-- -----------------------------------------------------

-- ~
CREATE TABLE IF NOT EXISTS `projectdb`.`user` (
  `user_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE INDEX `username_UNIQUE` (`username` ASC) VISIBLE)
ENGINE = InnoDB;
-- ~

-- -----------------------------------------------------
-- Table `projectdb`.`project`
-- -----------------------------------------------------

-- ~
CREATE TABLE IF NOT EXISTS `projectdb`.`project` (
  `project_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `project_name` VARCHAR(45) NOT NULL,
  `project_description` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`project_id`))
ENGINE = InnoDB;
-- ~

-- -----------------------------------------------------
-- Table `projectdb`.`user_project`
-- -----------------------------------------------------

-- ~
CREATE TABLE IF NOT EXISTS `projectdb`.`user_project` (
  `user_project_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `user_id` INT UNSIGNED NOT NULL,
  `project_id` INT UNSIGNED NOT NULL,
  `date_added` DATE NOT NULL,
  `last_updated_by` INT UNSIGNED NULL,
  `last_update_date` DATE NOT NULL,
  PRIMARY KEY (`user_project_id`),
  INDEX `user_project_fk1_idx` (`user_id` ASC) VISIBLE,
  INDEX `user_projcet_fk2_idx` (`project_id` ASC) VISIBLE,
  INDEX `user_project_fk3_idx` (`last_updated_by` ASC) VISIBLE,
  CONSTRAINT `user_project_fk1`
    FOREIGN KEY (`user_id`)
    REFERENCES `projectdb`.`user` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `user_project_fk2`
    FOREIGN KEY (`project_id`)
    REFERENCES `projectdb`.`project` (`project_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `user_project_fk3`
    FOREIGN KEY (`last_updated_by`)
    REFERENCES `projectdb`.`user` (`user_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;
-- ~