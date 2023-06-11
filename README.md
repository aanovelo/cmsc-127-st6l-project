# OWEDIO: CMSC 127 ST6L PROJECT

# DEVELOPERS
Gonzales, Katrina 
Novelo, Aljon
Repaso, Laurenz
Zapanta, Mark

# SETUP
1. Install the dependencies by running `pip install -r dependencies.txt`
2. Create a user, database, and tables by logging into the `root` user
```
    sudo mariadb
    source <path of userdb_setup.sql>
    quit;
```
*Note:*
*Use the absolute path of userdb_setup.sql (ex. `source /Users/aljonnovelo/Desktop/cmsc-127-st6l-project/userdb_setup.sql`)*
3. Run `python3 main.py`

# DESCRIPTION
This information system is designed to record and manage data related to owed money from friend or group expenses. It provides a flexible and realistic database design along with a well-implemented solution using a chosen programming language (PL) and a relational database management system (RDBMS). The system allows users to add, delete, search, and update expenses, friends, and groups, enabling efficient tracking and management of financial transactions.

# FEATURES
Expense Management:
1. Add a new expense: Users can record a new expense, including details such as the transaction amount, date, involved users, and group  (if applicable).
2. Delete an expense: Users can remove an existing expense from the system, ensuring accurate data management.
3. Search expenses: Users can search for specific expenses based on different criteria like date, amount, user, or group, facilitating   easy retrieval of relevant information.
4. Update an expense: Users can modify the details of an existing expense, allowing for corrections or updates to reflect accurate information.

Friend Management:
1. Add a new friend: Users can add new friends to the system, providing their details such as name, contact information, and any additional relevant information.
2. Delete a friend: Users can remove a friend from the system when necessary, ensuring the data remains up-to-date.
3. Search friends: Users can search for specific friends using various search parameters such as name or contact information, making it easy to find and manage friend records.
4. Update a friend: Users can update the information of an existing friend, such as contact details or any other relevant information.

Group Management:
1. Add a new group: Users can create new groups for managing shared expenses, specifying the group name and any additional relevant information.
2. Delete a group: Users can delete a group from the system, ensuring efficient management of groups and their associated expenses.
3. Search groups: Users can search for specific groups using parameters like the group name, enabling easy access to group information.
4. Update a group: Users can update the details of an existing group, such as modifying the group name or adding/removing group members.

Reports to be generated:

1. View all expenses made within a month: Generates a report displaying all expenses recorded within a specified month, providing an overview of financial transactions during that period.
2. View all expenses made with a friend: Generates a report showing all expenses involving a specific friend, allowing users to track their financial transactions with that individual.
3. View all expenses made with a group: Generates a report presenting all expenses associated with a particular group, enabling users to monitor shared expenses within the group.
4. View current balance from all expenses: Generates a report showcasing the current balance for each user based on their recorded expenses, facilitating financial tracking and management.
5. View all friends with outstanding balance: Generates a report listing all friends who have outstanding balances, helping users identify individuals who owe or are owed money.
6. View all groups: Generates a report displaying all created groups, providing an overview of the existing groups within the system.
7. View all groups with an outstanding balance: Generates a report presenting all groups with outstanding balances, assisting users in identifying groups with financial discrepancies or unpaid expenses.







