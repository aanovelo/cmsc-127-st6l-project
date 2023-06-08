import friend
import expense
import group
import view

def expense_function():
    print("[1] Add an expense")
    print("[2] Delete an expense")
    print("[3] Search an expense")
    print("[4] Update an expense")
    print("[5] View an expense")
    print("[6] Show All Expenses")


    choice_1 = input("Enter the number corresponding to the feature you want to choose: ")
    
    if choice_1 == '1':
        expense.addExpense()
    elif choice_1 == '2':
        expense.deleteExpense()
    elif choice_1 == '3':
        expense.searchExpense()
    elif choice_1 == '4':
        expense.updateExpense()
    elif choice_1 == '5':
        expense.viewExpense()
    elif choice_1 == '6':
        expense.printExpenses()        
    else:
        print("Invalid choice!")

def friend_function():
    print("[1] Add a friend")
    print("[2] Delete a friend")
    print("[3] Search a friend")
    print("[4] Update a friend")
    print("[5] View a friend")
    print("[6] Print friends")
    print("[7] Exit")

    choice_2 = input("Enter the number corresponding to the feature you want to choose: ")
    
    if choice_2 == '1':
        friend.addFriend()
    elif choice_2 == '2':
        friend.deleteFriend()
    elif choice_2 == '3':
        friend.searchFriend()
    elif choice_2 == '4':
        friend.updateFriend()
    elif choice_2 == '5':
        friend.viewFriend()
    elif choice_2 == '6':
        friend.printFriends()
    elif choice_2 == '7':
        print("Exiting...")
    else:
        print("Invalid choice!")

def group_function():
    print("[1] Add a group")
    print("[2] Delete a group")
    print("[3] Search a group")
    print("[4] Update a group")
    print("[5] View a group")
    print("[6] Print all groups")


    choice_3 = input("Enter the number corresponding to the feature you want to choose: ")
    
    if choice_3 == '1':
        group.addGroup()
    elif choice_3 == '2':
        group.deleteGroup()
    elif choice_3 == '3':
        group.searchGroup()
    elif choice_3 == '4':
        group.updateGroup()
    elif choice_3 == '5':
        group.viewGroup()
    elif choice_3 == '6':
        group.printGroups()
    else:
        print("Invalid choice!")

def view_owedio():
    print("[1] View all expenses made within a month;")
    print("[2] View all expenses made with a friend")
    print("[3] View all expenses made with a group")
    print("[4] View current balance from all expenses")
    print("[5] View all friends with outstanding balance")
    print("[6] View all groups")
    print("[7] View all groups with an outstanding balance")

    choice_4 = input("Enter the number corresponding to the feature you want to choose: ")

    if choice_4 == '1':
        view.expense_within_month()
    elif choice_4 == '2':
        view.expenses_with_friend
    elif choice_4 == '3':
        view.expense_with_grp
    elif choice_4 == '4':
        view.current_balance
    elif choice_4 == '5':
        view.view_all_groups_w_balance
    elif choice_4 == '6':
        view.view_all_groups
    elif choice_4 == '7':
        view.view_all_groups_w_balance
    else:
        print("Invalid choice!")

def menu():
    print("WELCOME TO OWEDIO")
    
    # menu will be printed over and over until the user exits the program
    while True:
        print("[1] Add, delete, search, and update an expense")
        print("[2] Add, delete, search, and update a friend")
        print("[3] Add, delete, search, and update a group")
        print("[4] View")
        print("[5] Exit")
    
        # asks for user's input
        choice = input("Enter the number corresponding to the feature you want to choose: ")
    
        # calls for the correspanding functions
        if choice == '1':
            expense_function()
        elif choice == '2':
            friend_function()
        elif choice == '3':
            group_function()
        elif choice == '4':
            group_function()
        elif choice == '5':
            print("Thank you for useing OWEDIO")
            break
        # invlalid choice prompt
        else:
            print("Invalid choice!\n")

menu()
