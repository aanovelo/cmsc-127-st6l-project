from connect import cnx, cursor
from tabulate import tabulate

# add a friend
def addFriend():
    friend_name = input("Enter the name of your friend: ")
    
    # insert a friend
    sql = "INSERT INTO user_friend (user_id, friend) VALUES (%s,%s)"

    # pass the parameter
    cursor.execute(sql, (1,friend_name))
    cnx.commit()

    # print success message
    print(f"Friend '{friend_name}' added successfully!")

    # check the table
    printFriends()

# delete a friend
def deleteFriend():
    # show the list of friends for user_id = 1
    cursor.execute("SELECT friend FROM user_friend WHERE user_id=1")
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

    friend_name = friends[friend_index][0]

    # delete the selected friend
    sql = "DELETE FROM user_friend WHERE friend = %s"
    cursor.execute(sql, (friend_name,))
    cnx.commit()

    if cursor.rowcount > 0:
        print(f"Friend '{friend_name}' deleted successfully!")
    else:
        print(f"Friend '{friend_name}' not found.")

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

# update a friend
def updateFriend():
    # get the list of friends
    cursor.execute("SELECT friend FROM user_friend")
    friends = cursor.fetchall()

    # print the list
    print("List of Friend Names:")
    table = tabulate(enumerate(friends, start=1), headers=["#", "Friend Name"], tablefmt="psql")
    print(table)
    print()

    # ask the user which friend to update
    friend_index = int(input("Enter the number corresponding to the friend you want to update: ")) - 1

    if friend_index < 0 or friend_index >= len(friends):
        print("Invalid friend index.")
        return

    # ask the user for a new name
    new_name = input("Enter the new name for the friend: ")

    # Update the name of the selected friend
    friend = friends[friend_index]
    sql = "UPDATE user_friend SET friend = %s WHERE friend = %s"
    cursor.execute(sql, (new_name, friend[0]))
    cnx.commit()

    print("Friend name updated successfully.")
    printFriends()

# view a friend
def viewFriend():
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

# this is just to check if it was successful
def printFriends():
    cursor.execute('SELECT * FROM user_friend')  
    col = [desc[0] for desc in cursor.description]
    row = cursor.fetchall()
    table = tabulate(row, headers=col, tablefmt='psql')
    print(table)