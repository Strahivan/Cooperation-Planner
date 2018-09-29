CREATE DATABASE IF NOT EXISTS urlinput;
CREATE TABLE IF NOT EXISTS 'urlinput.'url'(
        'index' INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
        'url' varchar(255), statuscode varchar(255),
        'tld' varchar(255), status varchar(255),
        'inLink' varchar(255),
        PRIMARY KEY ('id'));
USE urlinput;
insert into url (url, statuscode, tld, status, inLink) VALUES ( 'cloudwards.net', '200', '.net', 'okay', '0');
INSERT INTO url VALUES ( 'Facebook.com', '200', '.com', 'okay', '0');
INSERT INTO url VALUES ( 'Xing.de', '200', '.de', 'okay', '0');