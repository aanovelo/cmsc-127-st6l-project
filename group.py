from connect import cnx, cursor
from tabulate import tabulate
from mysql.connector import Error

# cursor = cnx.cursor()

def addGroup():
    try:
        user_id = 1
        group_name = input("Enter the name of your group: ")
        # Insert the group into the user_group table
        sql = "INSERT INTO user_group (user_id, group_name) VALUES (%s, %s)"
        cursor.execute(sql, (user_id, group_name))
        cnx.commit()

        print(f"Group '{group_name}' added successfully!")

    except Error as e:
        print("An error occurred while adding the group:", str(e))


def deleteGroup():
    try:
        cursor.execute("SELECT group_id, group_name FROM user_group WHERE user_id=1")
        groups = cursor.fetchall()
        print(groups)
        print("List of groups:")
        table = tabulate(enumerate(groups, start=1), headers=["#", "Group"], tablefmt="psql")
        print(table)
        print()

        # ask the user for input
        groupIndex = int(input("Enter the number corresponding to the group you want to delete: ")) - 1
        
        if groupIndex < 0 or groupIndex >= len(groups):
            print("Invalid friend index.")
            return

        groupToDelete = groups[groupIndex]
        print(groupToDelete)

        # delete associated rows from transaction_debitor table
        delete_members = "DELETE FROM group_member WHERE group_id = %s"
        cursor.execute(delete_members, (groupToDelete[0],))
        cnx.commit()
        
        # fetch all transactions group_id = grouptodlete
        fetchGroupTransaction = "SELECT transaction_id FROM app_transaction WHERE group_id = %s"
        cursor.execute(fetchGroupTransaction, (groupToDelete[0],))
        groupTransaction = cursor.fetchall()
        print(f"Group transactions: {groupTransaction}")

        # for loop sa debitor at creditor ung transac_id
        deleteDebitors = "DELETE FROM transaction_debitor WHERE transaction_id = %s"
        for groupDebitor in groupTransaction:
            cursor.execute(deleteDebitors, (groupDebitor[0],))
            cnx.commit()

        deleteCreditors = "DELETE FROM transaction_creditor WHERE transaction_id = %s"
        for groupCreditor in groupTransaction:
            cursor.execute(deleteCreditors, (groupCreditor[0],))
            cnx.commit()

        # # Delete the group transactions from the app_transaction table
        delete_transactions = "DELETE FROM app_transaction WHERE group_id = %s"
        cursor.execute(delete_transactions, (groupToDelete[0],))
        cnx.commit()

        # # Delete the group from the user_group table
        delete_group = "DELETE FROM user_group WHERE group_id = %s"
        cursor.execute(delete_group, (groupToDelete[0],))
        cnx.commit()

        if cursor.rowcount > 0:
            print(f"Group with ID '{groupToDelete[1]}' and all its contents deleted successfully!")
        else:
            print(f"Group with ID '{groupToDelete[1]}' not found.")
        printGroups()


    except Error as e:
        print("An error occurred while deleting the group:", str(e))

    # finally:
    #     cursor.close()
    #     cnx.close()
    #     # print("Connection closed.")


def searchGroup():
    try:
        group_name = input("Enter the name of the group you want to search: ")
        # Search for the group by name
        sql = "SELECT * FROM user_group WHERE group_name LIKE %s"
        cursor.execute(sql, (group_name,))
        results = cursor.fetchall()

        if len(results) > 0:
            print("Search Results:")
            table = tabulate(results, headers=["Group ID", "User ID", "Group Name", "Group Outstanding", "Total Expense"],
                             tablefmt="psql")
            print(table)
        else:
            print(f"No results found for group '{group_name}'.")


    except Error as e:
        print("An error occurred while searching for groups:", str(e))

    # finally:
        # cursor.close()
        # cnx.close()
        # print("Connection closed.")


def updateGroup():
    try:
        cursor.execute("SELECT group_id, group_name FROM user_group WHERE user_id=1")
        groups = cursor.fetchall()
        print(groups)
        print("List of groups:")
        table = tabulate(enumerate(groups, start=1), headers=["#", "Group"], tablefmt="psql")
        print(table)
        print()

        groupIndex = int(input("Enter the number corresponding to the group you want to update: ")) - 1
        
        if groupIndex < 0 or groupIndex >= len(groups):
            print("Invalid friend index.")
            return

        groupToUpdate = groups[groupIndex]
        print(groupToUpdate)

        newGroupName = str(input("Enter new group name: "))
        # Update the name of the group
        sql = "UPDATE user_group SET group_name = %s WHERE group_id = %s"
        cursor.execute(sql, (newGroupName, groupToUpdate[0]))
        cnx.commit()

        # print(f"Group with ID '{group_id}' updated successfully.")

    except Error as e:
        print("An error occurred while updating the group:", str(e))

    printGroups()
    # finally:
        # cursor.close()
        # cnx.close()
        # print("Connection closed.")


def viewGroup():
    try:
        # Retrieve all groups
        sql = "SELECT * FROM user_group"
        cursor.execute(sql)
        groups = cursor.fetchall()

        # Print the list of groups
        print("List of Groups:")
        table = tabulate(groups, headers=["Group ID", "User ID", "Group Name", "Group Outstanding", "Total Expense"],
                         tablefmt="psql")
        print(table)

    except Error as e:
        print("An error occurred while viewing the groups:", str(e))

    # finally:
        # cursor.close()
        # cnx.close()
        # print("Connection closed.")


def printGroups():
    try:
        # Retrieve all groups
        cursor.execute("SELECT * FROM user_group WHERE user_id = 1")
        groups = cursor.fetchall()

        groupNames = []
        for group in groups:
            groupNames.append(group[2])
        # Print the list of groups
        print("List of Groups:")
        table = tabulate(enumerate(groupNames,start=1), headers=["Choice", "Group Name"],
                        tablefmt="psql")
        print(table)
    
    except Error as e:
        print("An error occurred while printing the groups:", str(e))

    # finally:
    #     cursor.close()
    #     cnx.close()
        # print("Connection closed.")

