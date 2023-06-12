from connect import cnx, cursor
from tabulate import tabulate

# view the sum of expenses made within a month
def expense_within_month(month, year):
    query = f"SELECT SUM(amount) as total_expenses FROM app_transaction WHERE MONTH(transaction_date) = {month} AND YEAR(transaction_date) = {year}"
    cursor.execute(query)
    result = cursor.fetchone()
    total_expenses = result[0]
    print("Total expenses within the month: $", total_expenses)

# view the sum of expenses made with a friend
def expenses_with_friend(friend_name):
    query = f"SELECT SUM(amount) as total_expenses FROM app_transaction at JOIN user_friend uf ON at.user_id = uf.user_id WHERE uf.friend = '{friend_name}'"
    cursor.execute(query)
    result = cursor.fetchone()
    total_expenses = result[0]
    print("Total expenses with friend: $", total_expenses)

# view the sum of expenses made with a group
def expense_with_grp(group_id):
    query = f"SELECT SUM(amount) as total_expenses FROM app_transaction at JOIN user_group ug ON at.group_id = ug.group_id WHERE ug.group_id = {group_id}"
    cursor.execute(query)
    result = cursor.fetchone()
    total_expenses = result[0]
    print("Total expenses with the group: $", total_expenses)
# view current balance from all expenses
def current_balance():
    query = "SELECT user_id, username, current_bal - user_outstanding AS balance FROM app_user"
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [i[0] for i in cursor.description]
    print(tabulate(result, headers=headers))

# view all friends with outstanding balance
def view_with_balance():
    query = "SELECT au.user_id, au.username, uf.friend, uf.friend_id, uf.outstanding_balance FROM app_user au JOIN user_friend uf ON au.user_id = uf.user_id WHERE uf.outstanding_balance > 0"
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
