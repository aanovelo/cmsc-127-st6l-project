-- CREATE TABLES
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
    CONSTRAINT fk_friend_friend FOREIGN KEY(friend_id) REFERENCES app_user(user_id),
    PRIMARY KEY(friend_id)
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
    friend_id INT NOT NULL,
    CONSTRAINT fk_transaction_id_debitor FOREIGN KEY(transaction_id) REFERENCES app_transaction(transaction_id),
    CONSTRAINT fk_friend_id_debitor FOREIGN KEY(friend_id) REFERENCES user_friend(friend_id)
);


-- NOTE: All data used in this section are just sample data

--INSERT

--INSERT INTO APP_USER TABLE
INSERT INTO app_user (user_id, username, email, current_bal, monthly_expense, user_outstanding, debt) VALUES (12345678, "mrzapanta", "mrzapanta1@up.edu.ph", 1500.69, 12500.69, 7500.69, 2456.69);
--INSERT INTO USER_FRIEND TABLE
INSERT INTO user_friend (user_id, friend) VALUES (87654321, "jepoydizon");
--INSERT INTO USER_GROUP TABLE
INSERT INTO user_group (group_id, user_id, group_name, group_outstanding, total_expense) VALUES (12458765, 12340987, "teamba", 1500.69, 15000.69);
--INSERT INTO APP_TRANSACTION TABLE
INSERT INTO app_transaction (transaction_id, user_id, group_id, split_amount, transaction_date) VALUES (12345678, 87654321, 12348765, 1500.69, "2023-05-24");
--INSERT INTO TRANSCATION_CREDITOR TABLE
INSERT INTO transaction_creditor (transaction_id, creditor) VALUES (12345678, "uysiidolpalatoheh");
--INSERT INTO TRANSCATION_DEBITOR TABLE
INSERT INTO transaction_debitor (transaction_id, creditor) VALUES (12345678, "siidolpalatoehuy");

-- SELECT
-- RETRIEVE ALL USERS FROM THE app_user TABLE:
SELECT * FROM app_user;

-- RETRIEVE USERNAMES AND EMAIL ADDRESSES OF ALL USERS FROM THE app_user TABLE:
SELECT username, email FROM app_user;

-- RETRIEVE THE TOTAL OUTSTANDING DEBT FOR EACH USER FROM THE app_user TABLE:
SELECT user_id, user_outstanding FROM app_user;

-- RETRIEVE THE USERNAMES AND CORRESPONDING GROUP NAMES FOR ALL USERS WHO BELONG TO A GROUP FROM THE user_group TABLE:
SELECT au.username, ug.group_name 
FROM app_user au 
JOIN user_group ug ON au.user_id = ug.user_id;

-- RETRIEVE THE TRANSACTION IDS AND SPLIT AMOUNTS FOR ALL TRANSACTIONS FROM THE app_transaction TABLE:
SELECT transaction_id, split_amount FROM app_transaction;

-- RETRIEVE THE CREDITORS AND DEBTORS INVOLVED IN A SPECIFIC TRANSACTION FROM THE transaction_creditor AND transaction_debitor TABLES:
SELECT tc.creditor, td.debitor
FROM transaction_creditor tc
JOIN transaction_debitor td ON tc.transaction_id = td.transaction_id
WHERE tc.transaction_id = 12345678;

-- RETRIEVE THE TOTAL EXPENSES AND OUTSTANDING AMOUNT FOR A SPECIFIC GROUP FROM THE user_group TABLE:
SELECT total_expense, group_outstanding
FROM user_group
WHERE group_id = 12345678;

-- RETRIEVE ALL FRIENDS OF A SPECIFIC USER FROM THE user_friend TABLE:
SELECT friend
FROM user_friend
WHERE user_id = 12345678;


-- UPDATE AN EXPENSE
    -- UPDATE SPLIT AMOUNT
    UPDATE app_transaction SET split_amount=30 WHERE transaction_id=11111111;
    
    -- UPDATE TRANSACTION DATE
    UPDATE app_transaction SET transaction_date="2002-12-30" WHERE transaction_id=11111111;


-- UPDATE A FRIEND
    -- UPDATE NAME OF A FRIEND
    UPDATE user_friend SET friend="Aljon" WHERE friend="Aljohn" AND user_id=12345678;

-- UPDATE A GROUP
    -- UPDATE A GROUP NAME
    UPDATE user_group SET group_name="Samgyup Pipol" WHERE group_id=11111111;

    -- UPDATE OUTSTANDING BALANCE
    UPDATE user_group SET group_outstanding=group_outstanding-(SELECT split_amount FROM app_transaction WHERE transaction_id=11111111) WHERE group_id=11111111;

    -- update expense
    UPDATE user_group SET total_expense= total_expense + (SELECT COUNT(debitor)*split_amount FROM transaction_debitor t JOIN app_transaction a ON t.transaction_id = a.transaction_id WHERE a.transaction_id=11111111) WHERE group_id=11111111;

-- DELETE

-- DELETES A USER
DELETE FROM app_user
WHERE user_id=12345678;

-- DELETES A USER'S FRIEND
DELETE FROM user_friend
WHERE user_id=12345678;

-- DELETES GROUP
DELETE FROM user_group
WHERE group_id=11111111;

-- DELETES APP TRANSACTION IF MORE THAN 3 YEARS
DELETE FROM app_transaction
WHERE DATEDIFF(YEAR(app_transaction),CURDATE())>3;

-- DELETES TRANSACTION CREDIT
DELETE FROM transaction_creditor
WHERE transaction_id=12345678;

-- DELETES TRANSACTION DEBIT
DELETE FROM transaction_debitor
WHERE transaction_id=12345678;

-- DELETING ALL DATA
DROP TABLE app_user;
DROP TABLE user_friend;
DROP TABLE user_group;
DROP TABLE app_transaction;
DROP TABLE transaction_creditor;
DROP TABLE transaction_debitor;