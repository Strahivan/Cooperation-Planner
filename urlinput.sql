CREATE DATABASE urlinput;
CREATE TABLE `urlinput.`url` (
        `id` INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        `URL` varchar(255), Statuscode varchar(255),
        `TLD` varchar(255), Status varchar(255),
        `Inlink` varchar(255),
        PRIMARY KEY (`id`));
USE urlinput;
insert into url (URL, Statuscode, TLD, Status, InLink) VALUES ("test", "test", "test", "test", "test");
