from connect import cnx, cursor
from tabulate import tabulate
from mysql.connector import Error


def addGroup(user_id, group_name):
    try:
        # Insert the group into the user_group table
        sql = "INSERT INTO user_group (user_id, group_name) VALUES (%s, %s)"
        cursor.execute(sql, (user_id, group_name))
        cnx.commit()

        print(f"Group '{group_name}' added successfully!")

    except Error as e:
        print("An error occurred while adding the group:", str(e))

    finally:
        cursor.close()
        cnx.close()
        print("Connection closed.")


def deleteGroup(group_id):
    try:
        # Delete the group from the user_group table
        sql = "DELETE FROM user_group WHERE group_id = %s"
        cursor.execute(sql, (group_id,))
        cnx.commit()

        if cursor.rowcount > 0:
            print(f"Group with ID '{group_id}' deleted successfully!")
        else:
            print(f"Group with ID '{group_id}' not found.")

    except Error as e:
        print("An error occurred while deleting the group:", str(e))

    finally:
        cursor.close()
        cnx.close()
        print("Connection closed.")


def searchGroup(group_name):
    try:
        # Search for the group by name
        sql = "SELECT * FROM user_group WHERE group_name = %s"
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

    finally:
        cursor.close()
        cnx.close()
        print("Connection closed.")


def updateGroup(group_id, new_group_name):
    try:
        # Update the name of the group
        sql = "UPDATE user_group SET group_name = %s WHERE group_id = %s"
        cursor.execute(sql, (new_group_name, group_id))
        cnx.commit()

        print(f"Group with ID '{group_id}' updated successfully.")

    except Error as e:
        print("An error occurred while updating the group:", str(e))

    finally:
        cursor.close()
        cnx.close()
        print("Connection closed.")


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

    finally:
        cursor.close()
        cnx.close()
        print("Connection closed.")


def printGroups():
    try:
        # Retrieve all groups
        cursor.execute("SELECT * FROM user_group")
        groups = cursor.fetchall()

        # Print the list of groups
        print("List of Groups:")
        table = tabulate(groups, headers=["Group ID", "User ID", "Group Name", "Group Outstanding", "Total Expense"],
                         tablefmt="psql")
        print(table)
    
    except Error as e:
        print("An error occurred while printing the groups:", str(e))

    finally:
        cursor.close()
        cnx.close()
        print("Connection closed.")


