CREATE DATABASE IF NOT EXISTS urlinput;
CREATE TABLE IF NOT EXISTS 'urlinput.'url'(
        'id' INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        'URL' varchar(255), Statuscode varchar(255),
        'TLD' varchar(255), Status varchar(255),
        'Inlink' varchar(255),
        PRIMARY KEY ('id'));
USE urlinput;
insert into url (url, statuscode, tld, status, inLink) VALUES ( 'cloudwards.net', '200', '.net', 'okay', '0');
INSERT INTO url VALUES ( 'Facebook.com', '200', '.com', 'okay', '0');
INSERT INTO url VALUES ( 'Xing.de', '200', '.de', 'okay', '0');