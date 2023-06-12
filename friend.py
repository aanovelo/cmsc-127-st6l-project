from connect import cnx, cursor
from tabulate import tabulate
import expense
from mysql.connector import Error

# add a friend
def addFriend():
    friend_name = input("Enter the name of your friend: ")
    
    # insert a friend
    addUser = "INSERT INTO app_user(username) VALUES (%s)"
    cursor.execute(addUser, (friend_name,))

    
    sql2 = "SELECT * FROM app_user ORDER BY user_id DESC LIMIT 1" #get the last row of app_user
    cursor.execute(sql2)
    lastRow = cursor.fetchone()
    print(lastRow)

    sql = "INSERT INTO user_friend VALUES (%s,%s,%s)"

    # pass the parameter
    cursor.execute(sql, (1,lastRow[0],friend_name))
    cnx.commit()

    # print success message
    print(f"Friend '{friend_name}' added successfully!")

    # check the table
    printFriends()


# delete a friend
def deleteFriend():
    cursor.execute("SELECT f.friend, f.friend_id FROM user_friend f NATURAL JOIN app_user a WHERE f.user_id=1")
    friends = cursor.fetchall()
    print(friends)
    print("List of Friends:")
    table = tabulate(enumerate(friends, start=1), headers=["#", "Friend"], tablefmt="psql")
    print(table)
    print()

    # ask the user for input
    friend_index = int(input("Enter the number corresponding to the friend you want to delete: ")) - 1
    
    if friend_index < 0 or friend_index >= len(friends):
        print("Invalid friend index.")
        return

    friendToDelete = friends[friend_index]
    print(friendToDelete)

    # delete associated rows from transaction_debitor table
    deleteTransactionDebitor = "DELETE FROM transaction_debitor WHERE transaction_id IN (SELECT transaction_id FROM app_transaction WHERE friend_id = %s)"
    cursor.execute(deleteTransactionDebitor, (friendToDelete[1],))
    cnx.commit()

    # delete the selected friend
    deleteCreditor = "DELETE FROM transaction_creditor WHERE creditor_id = %s"
    cursor.execute(deleteCreditor, (friendToDelete[1],))
    cnx.commit()

    deleteTransaction = "DELETE FROM app_transaction WHERE friend_id = %s"
    cursor.execute(deleteTransaction, (friendToDelete[1],))
    cnx.commit()

    deleteMember = "DELETE FROM group_member WHERE member_id = %s"
    cursor.execute(deleteMember, (friendToDelete[1],))
    cnx.commit()

    sql = "DELETE FROM user_friend WHERE friend_id = %s"
    cursor.execute(sql, (friendToDelete[1],))
    cnx.commit()

    deleteUser = "DELETE FROM app_user WHERE user_id = %s"
    cursor.execute(deleteUser, (friendToDelete[1],))
    cnx.commit()

    if cursor.rowcount > 0:
        print(f"Friend '{friendToDelete}' deleted successfully!")
    else:
        print(f"Friend '{friendToDelete}' not found.")


    # check table
    printFriends()

# search a friend
def searchFriend():
    # ask the user for input
    friend_name = input("Enter the name of the friend you want to search for: ")

    # search the friend
    sql = "SELECT * FROM user_friend WHERE friend = %s"
    cursor.execute(sql, (friend_name,))
    results = cursor.fetchall()

    # show the friend
    if len(results) > 0:
        print("Search Results:")
        table = tabulate(results, headers=["User ID", "Friend"], tablefmt="psql")
        print(table)
    else:
        print(f"No results found for friend '{friend_name}'.")
    
    lastindex = 0
    for index, friend in enumerate(results,start=1):
        print(f"[{index}] View details of {friend[2]}")
        lastindex = index
    lastindex = lastindex + 1
    print(f"[{lastindex}] Exit")
    searchMenuInput = int(input("Choice: "))

    if searchMenuInput < 0 or searchMenuInput > lastindex:
        print("Invalid choice.")
        return
    
    if searchMenuInput == lastindex:
        return
    else:
        print(results[searchMenuInput - 1])
    # view details=

# update a friend
def updateFriend():
    # Get the list of friends
    cursor.execute("SELECT friend, friend_id FROM user_friend")
    friends = cursor.fetchall()

    # Print the list
    print("List of Friend Names:")
    table = tabulate(enumerate(friends, start=1), headers=["#", "Friend Name"], tablefmt="psql")
    print(table)
    print()

    # Ask the user which friend to update
    friend_index = int(input("Enter the number corresponding to the friend you want to update: ")) - 1

    if friend_index < 0 or friend_index >= len(friends):
        print("Invalid friend index.")
        return

    friend = friends[friend_index]
    print(friend)
    
    # Ask the user for a new name
    new_name = input("Enter the new name for the friend: ")

    # Update the name of the selected friend in user_friend table
    sql = "UPDATE user_friend SET friend = %s WHERE friend_id = %s"
    cursor.execute(sql, (new_name, friend[1]))

    # Update the name of the selected friend in app_user table
    update_username = "UPDATE app_user SET username = %s WHERE user_id = %s"
    cursor.execute(update_username, (new_name, friend[1]))

    cnx.commit()

    print("Friend name updated successfully.")
    printFriends()


# view a friend
def viewFriend(results):
    # get the list of friends
    cursor.execute("SELECT * FROM user_friend")
    friends = cursor.fetchall()

    # print the list
    print("List of Friends:")
    table = tabulate(enumerate(friends, start=1), headers=["#", "User ID", "Friend"], tablefmt="psql")
    print(table)
    print()

    # ask the user for input
    friend_index = int(input("Enter the number corresponding to the friend you want to view: ")) - 1
    
    if friend_index < 0 or friend_index >= len(friends):
        print("Invalid friend index.")
        return

    friend = friends[friend_index]

    # print the details
    print("Friend Details:")
    details = tabulate([friend], headers=["User ID", "Friend"], tablefmt="psql")
    print(details)

    print("[1] Create transaction")
    print("[2] Exit")
    choice1 = int(input("Enter your choice: "))
    if (choice1 == 1):
        expense.addExpense("Friend")
    elif (choice1 == 2):
        print("Exiting")

# this is just to check if it was successful
def printFriends():
    cursor.execute('SELECT * FROM user_friend')  
    col = [desc[0] for desc in cursor.description]
    row = cursor.fetchall()
    table = tabulate(enumerate(row, start=0), headers=["#",col], tablefmt='psql')
    print(table)

