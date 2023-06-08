from connect import cnx, cursor
from tabulate import tabulate
from mysql.connector import Error
import group
import friend

def addExpense():
    try:
        print("[1] Add expense to a group")
        print("[2] Add expense to a friend")
        inputUser = int(input("Input choice: "))

        if inputUser == 1:
            group.printGroups()
            groupChoice = int(input("Group choice: "))
        
        elif inputUser == 2:
            friend.printFriends()
            friendChoice = int(input("Friend choice: "))
            if friendChoice == 

        

        #ADD TO A GROUP
        #ADD TO A FRIEND

        
        # Get the input from the user
        viewFriend()
        
        
        friend_name = input("Enter the name of your friend: ")
        expense_amount = float(input("Enter the expense amount: "))

        # Retrieve the friend's ID from the database
        cursor.execute("SELECT user_id FROM user_friend WHERE friend = %s", (friend_name,))
        result = cursor.fetchone()

        if result is None:
            print(f"Friend '{friend_name}' not found.")
            return

        friend_id = result[0]

        # Insert the expense into the expenses table
        sql = "INSERT INTO app_transaction (user_id, group_id, split_amount, transaction_date) VALUES (%s, %s,%s, CURRENT_DATE())"
        cursor.execute(sql, (friend_id, 1, expense_amount))
        cnx.commit()

        # Retrieve the transaction ID
        transaction_id = cursor.lastrowid

        # Insert the creditor information
        sql_creditor = "INSERT INTO transaction_creditor (transaction_id, creditor) VALUES (%s, %s)"
        cursor.execute(sql_creditor, (transaction_id, friend_name))
        cnx.commit()

        print(f"Expense for friend '{friend_name}' added successfully!")
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

        # ask the user for input
        expense_index = int(input("Enter the number corresponding to the expense you want to delete: ")) - 1

        if expense_index < 0 or expense_index >= len(expenses):
            print("Invalid expense index.")
            return

        expense = expenses[expense_index]
        transaction_id = expense[0]

        # delete the selected expense
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
        # ask the user for input
        friend_name = input("Enter the name of the friend whose expenses you want to search for: ")

        # search the expenses
        sql = """
            SELECT t.transaction_id, f.friend, t.split_amount, t.transaction_date
            FROM app_transaction t
            INNER JOIN transaction_creditor c ON t.transaction_id = c.transaction_id
            INNER JOIN user_friend f ON c.creditor = f.friend
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


def updateExpense():
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

        # ask the user which expense to update
        expense_index = int(input("Enter the number corresponding to the expense you want to update: ")) - 1

        if expense_index < 0 or expense_index >= len(expenses):
            print("Invalid expense index.")
            return

        # ask the user for a new amount
        new_amount = float(input("Enter the new split amount for the expense: "))

        expense = expenses[expense_index]
        transaction_id = expense[0]

        # Update the amount of the selected expense
        sql = "UPDATE app_transaction SET split_amount = %s WHERE transaction_id = %s"
        cursor.execute(sql, (new_amount, transaction_id))
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
            SELECT t.transaction_id, f.friend, t.split_amount, t.transaction_date
            FROM app_transaction t
            INNER JOIN transaction_creditor c ON t.transaction_id = c.transaction_id
            INNER JOIN user_friend f ON c.creditor = f.friend
        """)
        expenses = cursor.fetchall()

        # print the expenses
        print("List of Expenses:")
        table = tabulate(expenses,
                         headers=["Transaction ID", "Friend", "Split Amount", "Transaction Date"],
                         tablefmt='psql')
        print(table)
        print()

    except Error as e:
        print("An error occurred while printing the expenses:", str(e))

    finally:
        cursor.close()
        cnx.close()
        # print("Connection closed.")
