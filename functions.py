import json
import time



def load_data(file_name):
    """This function loads data from a JSON file and returns the data as a dictionary."""
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def check_info(user, pwd):
    """This function checks if the username and password are correct or not.
    takes two arguments user and pwd and returns True if the username and password are correct"""

    print("Checking the information of the system")
    users_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    
    for user_data, password_data in zip(users_data.values(), password_data.values()):
        if user == user_data.get("user") and pwd == password_data.get("password"):
            return True, user_data.get("role")
    else:
        return False, False


def admin_panel():
    """This function is the admin panel. It is called when the user is an admin."""
    print("\n--------------------welcome to admin panel----------------------------------\n")
    choice = input("""
1: Add a student
2: Remove a student
3: View all users
4: Add an admin
5: Change password
6: Exit
Enter your choice:- """)
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        view_students()
    elif choice == "4":
        add_admin()
    elif choice == "5":
        user = input("Username:- ")
        pwd = input("\nPassword:- ")
        change_admin_password(user,pwd)
    elif choice == "6":
        exit()
    else:
        print("Invalid choice")
        admin_panel()
    
    
def add_student():
    """This function adds a student to the system."""
    print("Adding a student")
    users_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    grades_data = load_data('grades.txt')
    eca_data = load_data('eca.txt')
    user = input("Username:- ")
    password = input("Password:- ")
    role = "student"
    try:
        grades = int(input("Grades:- "))
    except ValueError:
        print("Invalid grade")
        add_student()

    eca = input("ECA:- ")
    
    max_key = max(users_data.keys(), default=0)
    new_key = str(int(max_key) + 1)
    users_data[new_key] = {"user": user, "role": role}
    password_data[new_key] = {"user": user, "password": password}
    grades_data[new_key] = {"user": user, "grade": grades}
    eca_data[new_key] = {"user": user, "club": eca}

    with open('users.txt', 'w') as file:
        json.dump(users_data, file)
    with open('passwords.txt', 'w') as file:
        json.dump(password_data, file)
    with open('grades.txt', 'w') as file:
            json.dump(grades_data, file)
    with open('eca.txt', 'w') as file:
            json.dump(eca_data, file)
    print("Student added successfully")
    admin_panel()

def add_admin():
    """This function adds an admin to the system."""
    print("Adding an admin")
    users_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    user = input("Username:- ")
    password = input("Password:- ")
    role = "admin"
    
    max_key = max(users_data.keys(), default=0)
    new_key = str(int(max_key) + 1)
    users_data[new_key] = {"user": user, "role": role}
    password_data[new_key] = {"user": user, "password": password}
    with open('users.txt', 'w') as file:
        json.dump(users_data, file)
    with open('passwords.txt', 'w') as file:
        json.dump(password_data, file)
    time.sleep(1)
    print("Admin added successfully")
    admin_panel()



def remove_student():
    """This function removes a student from the system."""
    print("Removing a student")
    users_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    grades_data = load_data('grades.txt')
    eca_data = load_data('eca.txt')
    user = input("Username:- ")
    for key, value in users_data.items():
        if user == value["user"]:
            if value["role"] == "admin":
                print("Error: You cannot remove an admin")
                admin_panel()
            else:
                users_data.pop(key) # pop le dictionary bata key remove garxa
                password_data.pop(key)
                
                for j, grade_data in grades_data.items():
                    if user == grade_data["user"]:
                        grades_data.pop(j)
                        break

                for k, eca_item in eca_data.items():
                    if user == eca_item["user"]:
                        eca_data.pop(k)
                        break
                
                with open('users.txt', 'w') as file:
                    json.dump(users_data, file)
                with open('passwords.txt', 'w') as file:
                    json.dump(password_data, file)
                with open('grades.txt', 'w') as file:
                    json.dump(grades_data, file)    
                with open('eca.txt', 'w') as file:
                    json.dump(eca_data, file)
                time.sleep(1)
                print("Student removed successfully")
                admin_panel()
    else:
        print("Student not found")
        remove_student()

def view_students():
    """This function views all the students in the system."""
    print("Viewing all users")
    time.sleep(1)
    users_data = load_data('users.txt')
    for key, value in users_data.items():
        user = value.get("user")
        role = value.get("role")
        print(f"User: {user}, Role: {role}")
    admin_panel()
     
def change_admin_password(user,pwd):
    """This function changes the password of an admin."""
    print("Changing password")
    password_data = load_data('passwords.txt')
    new_password = input("New password:- ")
    for key, value in password_data.items():
        if user == value["user"] and pwd == password_data[key]["password"]:
            password_data[key]["password"] = new_password
            with open('passwords.txt', 'w') as file:
                json.dump(password_data, file)
            print("Password changed successfully")
            time.sleep(1)
            admin_panel()  


def exit():
    """This function exits the program."""
    print("Exiting the program")
    quit()


def student_panel(user,pwd):
    """This function is the student panel. It is called when the user is a student."""
    print("\n-------------------------welcome to student panel----------------------------------\n")
    
    user_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    grades_data = load_data('grades.txt')
    eca_data = load_data('eca.txt')

    for _, value in user_data.items():
        if user == value["user"] and pwd == password_data[_]["password"]:
            print(f"User: {value['user']},\nRole: {value['role']},\nGrades: {grades_data[_]['grade']},\nECA: {eca_data[_]['club']}")
            break

    choice = input("""
1: Change password
2: Change club
3: Exit
    """)
    if choice == "1":
        change_password(user,pwd)
    elif choice == "2":
        change_club(user,pwd)
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        student_panel(user,pwd)

def change_password(user,pwd):
    """This function changes the password of a student."""
    print("Changing password")
    password_data = load_data('passwords.txt')
    new_password = input("New password:- ")
    for key, value in password_data.items():
        if user == value["user"] and pwd == password_data[key]["password"]:
            password_data[key]["password"] = new_password
            with open('passwords.txt', 'w') as file:
                json.dump(password_data, file)
            print("Password changed successfully")
            time.sleep(1)
            student_panel(user,pwd)
   

def change_club(user,pwd):
    """This function changes the club of a student."""
    print("Changing club")
    eca_data = load_data('eca.txt')
    password_data = load_data('passwords.txt')
    new_club = input("New club:- ")
    for key, value in eca_data.items():
        if user == value["user"] and pwd == password_data[key]["password"]:
            eca_data[key]["club"] = new_club
            with open('eca.txt', 'w') as file:
                json.dump(eca_data, file)
            print("Club changed successfully")
            time.sleep(1)
            student_panel(user,pwd)
    else:
        print("User not found")
        change_club(user,pwd)
    
    





