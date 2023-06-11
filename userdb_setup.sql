DROP DATABASE IF EXISTS proj;

CREATE OR REPLACE USER 'projectmanager'@'localhost' IDENTIFIED BY 'project';
CREATE DATABASE proj;
GRANT ALL ON proj.* TO 'projectmanager'@'localhost';

USE proj;

CREATE TABLE app_user (
    user_id INT AUTO_INCREMENT,
    username VARCHAR(15),
    email VARCHAR(320),
    current_bal FLOAT(7,2),
    monthly_expense FLOAT(7,2),
    user_outstanding FLOAT(7,2),
    debt FLOAT(7,2),
    PRIMARY KEY(user_id)
);

CREATE TABLE user_friend (
    user_id INT NOT NULL,
    friend_id INT NOT NULL,
    friend VARCHAR(40),
    CONSTRAINT fk_user_friend FOREIGN KEY(user_id) REFERENCES app_user(user_id),
    CONSTRAINT fk_friend_id FOREIGN KEY (friend_id) REFERENCES app_user(user_id),
);

CREATE TABLE user_group (
    group_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    group_name VARCHAR(15),
    group_outstanding FLOAT(7,2),
    total_expense FLOAT(7,2),
    PRIMARY KEY(group_id),
    CONSTRAINT fk_user_group FOREIGN KEY(user_id) REFERENCES app_user(user_id)
);

CREATE TABLE group_member (
    group_id INT,
    friend_id INT,
    CONSTRAINT fk_group_member_group FOREIGN KEY(group_id) REFERENCES user_group(group_id),
    CONSTRAINT fk_group_member_friend FOREIGN KEY(friend_id) REFERENCES user_friend(friend_id),
    PRIMARY KEY(group_id, friend_id)
);

CREATE TABLE app_transaction (
    transaction_id INT AUTO_INCREMENT,
    user_id INT NOT NULL,
    friend_id INT DEFAULT NULL,
    group_id INT DEFAULT NULL,
    split_amount FLOAT(7,2),
    transaction_date DATE,
    PRIMARY KEY(transaction_id),
    CONSTRAINT fk_user_transaction FOREIGN KEY(user_id) REFERENCES app_user(user_id),
    CONSTRAINT fk_group_transaction FOREIGN KEY(group_id) REFERENCES user_group(group_id),
    CONSTRAINT fk_friend_transaction FOREIGN KEY(friend_id) REFERENCES user_friend(friend_id)
);

CREATE TABLE transaction_creditor (
    transaction_id INT NOT NULL,
    creditor VARCHAR(40),
    CONSTRAINT fk_transaction_id_creditor FOREIGN KEY(transaction_id) REFERENCES app_transaction(transaction_id),
    CONSTRAINT u_creditor UNIQUE(creditor)
);

CREATE TABLE transaction_debitor (
    transaction_id INT NOT NULL,
    debitor VARCHAR(40),
    CONSTRAINT fk_transaction_id_debitor FOREIGN KEY(transaction_id) REFERENCES app_transaction(transaction_id),
    CONSTRAINT u_debitor UNIQUE(debitor) --dont make unique
);

insert into app_user(username) values("user1");
insert into app_user(username) values("user2");
insert into app_user(username) values("user3");
insert into app_user(username) values("user4");
insert into app_user(username) values("user5");

insert into user_friend(user_id,friend) values (1, "friend1");
insert into user_friend(user_id,friend) values (1, "friend2");
insert into user_friend(user_id,friend) values (1, "friend3");
insert into user_friend(user_id,friend) values (2, "friend4");
insert into user_friend(user_id,friend) values (2, "friend5");
insert into user_friend(user_id,friend) values (3, "friend6");

insert into user_group(user_id, group_name) values(1, "group1");
insert into user_group(user_id, group_name) values(1, "group2");
insert into user_group(user_id, group_name) values(1, "group3");
insert into user_group(user_id, group_name) values(2, "group4");
insert into user_group(user_id, group_name) values(2, "group5");
insert into user_group(user_id, group_name) values(3, "group6");

insert into group_member values(1,1);
insert into group_member values(1,2);
insert into group_member values(1,3);
insert into group_member values(1,4);