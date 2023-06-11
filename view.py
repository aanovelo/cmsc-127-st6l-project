from connect import cnx, cursor
from tabulate import tabulate

# view all expenses made within a month
def expense_within_month(): #gagawing SUM na lang itoo
    query = "SELECT * FROM app_transaction WHERE MONTH(transaction_date) = [month] AND YEAR(transaction_date) = [year]"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view all expenses made with a friend
def expenses_with_friend(): #gagawing SUM na lang itoo
    query = "SELECT at.* FROM app_transaction at JOIN user_friend uf ON at.user_id = uf.user_id WHERE uf.friend = '[friend_name]'"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view all expenses made with a group
def expense_with_grp(): #gagawing SUM na lang itoo
    query = "SELECT at.* FROM app_transaction at JOIN user_group ug ON at.group_id = ug.group_id WHERE ug.group_id = [group_id]"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view current balance from all expenses
def current_balance():
    query = "SELECT user_id, username, current_bal - user_outstanding AS balance FROM app_user"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view all friends with outstanding balance
def view_with_balance():
    query = "SELECT au.user_id, au.username, uf.friend, uf.user_id AS friend_user_id, au.user_outstanding FROM app_user au JOIN user_friend uf ON au.user_id = uf.user_id WHERE au.user_outstanding > 0"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view all groups
def view_all_groups():
    query = "SELECT * FROM user_group"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view all groups with an outstanding balance
def view_all_groups_w_balance():
    query = "SELECT ug.group_id, ug.group_name, ug.group_outstanding FROM user_group ug WHERE ug.group_outstanding > 0"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))
