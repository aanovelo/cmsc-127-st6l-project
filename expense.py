
from connect import cnx, cursor
from tabulate import tabulate
from mysql.connector import Error
import group
import friend

def addExpense():

    print("\n[1] Add expense to a group")
    print("[2] Add expense to a friend")
    inputUser = int(input("Input choice: "))

    if inputUser == 1:
        group.printGroups()
        groupChoice = int(input("Group choice: "))
        addExpenseToGroup(groupChoice)
    
    elif inputUser == 2:
        friend.printFriends()
        friendChoice = int(input("Friend choice: "))
        addExpenseToFriend(friendChoice)
        
def addExpenseToFriend(friendChoice):
    try:
        sql = "SELECT * from user_friend WHERE user_id=1"
        cursor.execute(sql)
        selectedFriend = cursor.fetchall()
        selectedFriendId = selectedFriend[friendChoice][1]
        print(selectedFriend[friendChoice])

        expense_amount = float(input("Enter the expense amount: "))
        print(f"Select\n[1] You\n[2] {selectedFriend[friendChoice][2]}")
        paidBy = int(input("Paid by: "))

        # Insert the expense into the expenses table
        sql = "INSERT INTO app_transaction (user_id, friend_id, split_amount, transaction_date) VALUES (%s,%s,%s, CURRENT_DATE())"
        cursor.execute(sql, (1,selectedFriendId,expense_amount/2))
        cnx.commit()

        sql2 = "SELECT * FROM app_transaction ORDER BY transaction_id DESC LIMIT 1" #get the last row of app_transaction
        cursor.execute(sql2)
        lastRow = cursor.fetchone()
        print(lastRow)
        
        if paidBy == 1:
            addDebitor = "INSERT INTO transaction_debitor values(%s, %s)"
            cursor.execute(addDebitor, (lastRow[0], selectedFriendId))
            addCreditor = "INSERT INTO transaction_creditor values (%s, %s)"
            cursor.execute(addCreditor, (lastRow[0], 1))
            cnx.commit()
        elif paidBy ==2:
            addCreditor = "INSERT INTO transaction_creditor values (%s, %s)"
            cursor.execute(addCreditor, (lastRow[0], selectedFriendId))
            addDebitor = "INSERT INTO transaction_debitor values(%s, %s)"
            cursor.execute(addDebitor, (lastRow[0], 1))
            cnx.commit()
        
        print(f"Expense for friend '{selectedFriend[friendChoice][2]}' added successfully!")
        printExpenses()

    except (ValueError, Error) as e:
        print("An error occurred while adding the expense:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")

def addExpenseToGroup(groupChoice):
    try:
        sql = "SELECT * from user_group WHERE user_id=1"
        cursor.execute(sql)
        selectedGroup = cursor.fetchall()
        selectedGroupId = selectedGroup[groupChoice][0]
        print(selectedGroup[groupChoice])
        
        expense_amount = float(input("Enter the expense amount: "))
        
        query_members = "SELECT * from group_member WHERE group_id = %s"
        cursor.execute(query_members, (selectedGroupId,))
        numberOfMembers = cursor.fetchall()

        print("\nSelect\n[1] You")

        friendName = "SELECT * from user_friend WHERE friend_id = %s"
        for index, member in enumerate(numberOfMembers, start=2):
            cursor.execute(friendName,(member[1],))
            frName = cursor.fetchone()
            print(f"[{index}] {frName[2]}")
        paidBy = int(input("Select friend who paid: "))

        sql1 = "INSERT INTO app_transaction (user_id, group_id, split_amount, transaction_date) VALUES (%s,%s,%s, CURRENT_DATE())"
        cursor.execute(sql1, (1,selectedGroupId, expense_amount/len(numberOfMembers)))
        cnx.commit()

        sql2 = "SELECT * FROM app_transaction ORDER BY transaction_id DESC LIMIT 1" #get the last row of app_transaction
        cursor.execute(sql2)
        lastRow = cursor.fetchone()
        print(lastRow)

        if paidBy == 1:
            # debitor = members
            addDebitor = "INSERT INTO transaction_debitor values(%s, %s)"
            for member in numberOfMembers:
                cursor.execute(addDebitor, (lastRow[0], member[1]))
            # creditor = you
            addCreditor = "INSERT INTO transaction_creditor values (%s, %s)"
            cursor.execute(addCreditor, (lastRow[0], 1))
            cnx.commit()
        else:
            # creditor = paidBy
            selectedFriendId = numberOfMembers[paidBy-2][1]  # Get the friend_id based on paidBy choice
            print(selectedFriendId)
            addCreditor = "INSERT INTO transaction_creditor values (%s, %s)"
            cursor.execute(addCreditor, (lastRow[0], selectedFriendId))
            # debitor = members-1 + you
            addDebitor = "INSERT INTO transaction_debitor values(%s, %s)"
            for member in numberOfMembers:
                if member[1] != selectedFriendId:
                    cursor.execute(addDebitor, (lastRow[0], member[1]))
            cursor.execute(addDebitor, (lastRow[0], 1))  # Add yourself as a debitor
            cnx.commit()

        print(f"Expense for group '{selectedGroup[groupChoice][2]}' added successfully!")
        printExpenses()

    except (ValueError, Error) as e:
        print("An error occurred while adding the expense:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")

def deleteExpense():
    try:
        # show the list of expenses
        cursor.execute("SELECT * FROM app_transaction")
        expenses = cursor.fetchall()

        # print the list
        print("List of Expenses:")
        table = tabulate(enumerate(expenses, start=0),
                         headers=["#", "Friend", "Split Amount", "Transaction Date"],
                         tablefmt="psql")
        print(table)
        print()

        # ask the user for input
        expense_index = int(input("Enter the number corresponding to the expense you want to delete: "))

        if expense_index < 0 or expense_index >= len(expenses):
            print("Invalid expense index.")
            return

        expense = expenses[expense_index]
        transaction_id = expense[0]

        # delete the selected expense
        deleteDebitor = "DELETE FROM transaction_debitor WHERE transaction_id = %s"
        cursor.execute(deleteDebitor,(transaction_id,))
        deleteCreditor = "DELETE FROM transaction_creditor WHERE transaction_id = %s"
        cursor.execute(deleteCreditor,(transaction_id,))
        sql_transaction = "DELETE FROM app_transaction WHERE transaction_id = %s"
        cursor.execute(sql_transaction, (transaction_id,))
        cnx.commit()

        if cursor.rowcount > 0:
            print(f"Expense with transaction ID '{transaction_id}' deleted successfully!")
        else:
            print(f"Expense with transaction ID '{transaction_id}' not found.")

        printExpenses()

    except (ValueError, Error) as e:
        print("An error occurred while deleting the expense:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")

def searchExpense():
    try:
        print("Search Options\n[1] Search by friend name\n[2]Search by group name")
        searchChoice = int(input("Choice: "))

        if searchChoice == 1:
            searchFriendExpense()
        elif searchChoice == 2:
            searchGroupExpense()
    except (ValueError, Error) as e:
        print("An error occurred while searching for expenses:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")

def searchFriendExpense():
    try:
        # ask the user for input
        friend_name = input("Enter the name of the friend whose expenses you want to search for: ")

        # search the expenses
        sql = """
            SELECT t.transaction_id, f.friend, t.split_amount, t.transaction_date
            FROM app_transaction t 
            NATURAL JOIN user_friend f
            WHERE f.friend = %s
        """
        cursor.execute(sql, (friend_name,))
        results = cursor.fetchall()

        # show the expenses
        if len(results) > 0:
            print(f"Search Results for expenses of friend '{friend_name}':")
            table = tabulate(results,
                             headers=["Transaction ID", "Friend", "Split Amount", "Transaction Date"],
                             tablefmt="psql")
            print(table)
        else:
            print(f"No expenses found for friend '{friend_name}'.")

    except (ValueError, Error) as e:
        print("An error occurred while searching for expenses:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")

def searchGroupExpense():
    try:
        # ask the user for input
        group_name = input("Enter the name of the group whose expenses you want to search for: ")

        # search the expenses
        sql = """
            SELECT t.transaction_id, f.group_name, t.split_amount, t.transaction_date
            FROM app_transaction t 
            NATURAL JOIN user_group f
            WHERE f.group_name = %s
        """
        cursor.execute(sql, (group_name,))
        results = cursor.fetchall()

        # show the expenses
        if len(results) > 0:
            print(f"Search Results for expenses of group '{group_name}':")
            table = tabulate(results,
                             headers=["Transaction ID", "Group", "Split Amount", "Transaction Date"],
                             tablefmt="psql")
            print(table)
        else:
            print(f"No expenses found for group '{group_name}'.")

    except (ValueError, Error) as e:
        print("An error occurred while searching for expenses:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")

def updateExpense():
    try:
        cursor.execute("""
            SELECT t.transaction_id,  t.friend_id, t.group_id, t.split_amount, t.transaction_date
            FROM app_transaction t WHERE t.transaction_date=CURDATE()
            """)
        expenses = cursor.fetchall()

        print("List of Transactions:")
        table = tabulate(enumerate(expenses, start=0),
                         headers=["#","Transaction ID", "Friend ID", "Group ID", "Split Amount", "Transaction Date"],
                         tablefmt='psql')
        print(table)
        print()

        # ask the user which expense to update
        expense_index = int(input("Enter the number corresponding to the expense you want to update: "))
        print(expenses[expense_index])

        if expense_index < 0 or expense_index >= len(expenses):
            print("Invalid expense index.")
            return

        # ask the user for a new amount
        new_amount = float(input("Enter the new expense to be shared: "))
        
        expense = expenses[expense_index]
        transaction_id = expense[0]
        print(transaction_id)

        sql2 = "SELECT friend_id FROM transaction_debitor WHERE transaction_id = %s"
        cursor.execute(sql2,(transaction_id,))
        count = cursor.fetchall()
        print(count)

        # Update the amount of the selected expense
        sql = "UPDATE app_transaction SET split_amount = %s WHERE transaction_id = %s"
        cursor.execute(sql, (new_amount/(count[0][0]+1), transaction_id))
        cnx.commit()

        print(f"Split amount for expense with transaction ID '{transaction_id}' updated successfully.")
        printExpenses()

    except (ValueError, Error) as e:
        print("An error occurred while updating the expense:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")


def viewExpenses():
    try:
        # get the list of expenses
        cursor.execute("""
            SELECT t.transaction_id, f.friend, t.split_amount, t.transaction_date
            FROM app_transaction t
            INNER JOIN transaction_creditor c ON t.transaction_id = c.transaction_id
            INNER JOIN user_friend f ON c.creditor = f.friend
        """)
        expenses = cursor.fetchall()

        # print the list
        print("List of Expenses:")
        table = tabulate(enumerate(expenses, start=1),
                         headers=["#", "Friend", "Split Amount", "Transaction Date"],
                         tablefmt="psql")
        print(table)
        print()

    except Error as e:
        print("An error occurred while viewing the expenses:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")


def printExpenses():
    try:
        cursor.execute("""
            SELECT t.transaction_id,  t.friend_id, t.group_id, t.split_amount, t.transaction_date
            FROM app_transaction t WHERE t.transaction_date=CURDATE()
            """)
        expenses = cursor.fetchall()

        # print the expenses
        print("List of Expenses:")
        table = tabulate(enumerate(expenses, start=0),
                         headers=["#","Transaction ID", "Friend ID", "Group ID", "Split Amount", "Transaction Date"],
                         tablefmt='psql')
        print(table)
        print()

    except Error as e:
        print("An error occurred while printing the expenses:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")