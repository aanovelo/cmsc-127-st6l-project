from connect import cnx, cursor
from tabulate import tabulate

# view the sum of expenses made within a month
def expense_within_month():
    print("\n===== YEAR 2023 =====")
    print("[1] January")
    print("[2] February")
    print("[3] March")
    print("[4] April")
    print("[5] May")
    print("[6] June")
    print("[7] July")
    print("[8] August")
    print("[9] September")
    print("[10] October")
    print("[11] November")
    print("[12] December")
    print("==================")
    selectedMonth = int(input("Select month: "))
    query = "SELECT SUM(split_amount) FROM app_transaction WHERE transaction_id IN (SELECT transaction_id FROM transaction_creditor WHERE creditor_id=1) and MONTH(transaction_date) = %s AND YEAR(transaction_date) = 2023"
    cursor.execute(query, (selectedMonth,))
    result = cursor.fetchone()
    total_expenses = result[0]
    if total_expenses:
        print(f"Total expenses within the month: PHP {total_expenses}")
    else:
        print(f"Total expenses within the month: {total_expenses}")

# view current balance from all expenses
def current_balance(yourBalance):
    query = "SELECT SUM(split_amount) FROM app_transaction WHERE transaction_id IN (SELECT transaction_id FROM transaction_creditor WHERE creditor_id=1)"
    cursor.execute(query)
    result = cursor.fetchone()
    total_expenses = result[0]
    print(f"Current Balance: PHP{yourBalance- total_expenses}")

# view all friends with outstanding balance
def view_with_balance():
    transacWithFriends = "select at.transaction_id, au.username, at.split_amount from app_transaction at join transaction_debitor td on at.transaction_id = td.transaction_id join app_user au on au.user_id = td.debitor_id where at.friend_id is not null and td.debitor_id != 1"
    cursor.execute(transacWithFriends)
    results = cursor.fetchall()

    print("\n===== FRIENDS WITH OUTSTANDING BALANCE =====")
    for index, friendOutBalance in enumerate(results,start=1):
        print(f"  {index}. {friendOutBalance[1]} - PHP{friendOutBalance[2]}")
    print("============================================")


# view all groups with an outstanding balance
def view_all_groups_w_balance():
    query = "select at.transaction_id, ug.group_name, sum(at.split_amount) from app_transaction at join user_group ug on at.group_id = ug.group_id join transaction_debitor td on at.transaction_id = td.transaction_id where at.group_id is not null group by at.group_id"
    cursor.execute(query)
    results = cursor.fetchall()

    print("\n===== GROUPS WITH OUTSTANDING BALANCE =====")
    for index, groupsWithBalance in enumerate(results,start=1):
        print(f"  {index}. {groupsWithBalance[1]} - PHP{groupsWithBalance[2]}")
    print("===========================================")
