def expense_function():
    print("[1] Add an expense")
    print("[2] Delete an expense")
    print("[3] Search an expense")
    print("[4] Update an expense")
    print("[5] View an expense")

    choice_1 = input("Enter the number corresponding to the feature you want to choose: ")
    
    # if choice_1 == '1':
        # call the function
    # elif choice_1 == '2':
        # call the function
    # elif choice_1 == '3':
        # call the function
    # elif choice_1 == '4':
         # call the function
    # elif choice_1 == '5':
         # call the function
    # else:
        #print("Invalid choice!")

def friend_function():
    print("[1] Add a friend")
    print("[2] Delete a friend")
    print("[3] Search a friend")
    print("[4] Update a friend")
    print("[5] View a friend")

    choice_2 = input("Enter the number corresponding to the feature you want to choose: ")
    
    # if choice_2 == '1':
        # call the function
    # elif choice_2 == '2':
        # call the function
    # elif choice_2 == '3':
        # call the function
    # elif choice_2 == '4':
         # call the function
    # elif choice_2 == '5':
         # call the function
    # else:
        #print("Invalid choice!")

def group_function():
    print("[1] Add a group")
    print("[2] Delete a group")
    print("[3] Search a group")
    print("[4] Update a group")
    print("[5] View a group")

    choice_3 = input("Enter the number corresponding to the feature you want to choose: ")
    
    # if choice_3 == '1':
        # call the function
    # elif choice_3 == '2':
        # call the function
    # elif choice_3 == '3':
        # call the function
    # elif choice_3 == '4':
         # call the function
    # elif choice_3 == '5':
         # call the function
    # else:
        #print("Invalid choice!")

def menu():
    print("WELCOME TO OWEDIO")
    
    # menu will be printed over and over until the user exits the program
    while True:
        print("[1] Add, delete, search, and update an expense;")
        print("[2] Add, delete, search, and update a friend;")
        print("[3] Add, delete, search, and update a group;")
        print("[4] Exit")
    
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
            print("Thank you for useing OWEDIO")
            break
        # invlalid choice prompt
        else:
            print("Invalid choice!\n")

menu()
