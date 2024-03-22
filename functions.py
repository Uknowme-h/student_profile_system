import json



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
    
    for i in range(1, len(users_data) + 1):
        if user == users_data[f"{i}"]["user"] and pwd == password_data[f"{i}"]["password"]:
            return True , users_data[f"{i}"]["role"]
    else:
        return False,False


def admin_panel():
    """This function is the admin panel. It is called when the user is an admin."""
    print("\n--------------------welcome to admin panel----------------------------------\n")
    choice = input("""
1: Add a student
2: Remove a student
3: View all students
4: Exit
Enter your choice:- """)
    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        view_students()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice")
        admin_panel()
    


def student_panel():
    """This function is the student panel. It is called when the user is a student."""
    print("\n--------------------welcome to student panel----------------------------------\n")
    print("Student panel is open")
    print("You can do whatever you want")
    
def add_student():
    """This function adds a student to the system."""
    print("Adding a student")
    users_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    grades_data = load_data('grades.txt')
    eca_data = load_data('eca.txt')
    user = input("Username:- ")
    password = input("Password:- ")
    role = input("Role:- ")
    grades = input("Grades:- ")
    eca = input("ECA:- ")
    
    users_data[len(users_data) + 1] = {"user": user, "role": role}
    password_data[len(password_data) + 1] = {"user":user,"password": password}
    grades_data[len(grades_data) + 1] = {"user":user,"grades": grades}
    eca_data[len(eca_data) + 1] = {"user":user,"eca": eca}

    with open('users.txt', 'w') as file:
        json.dump(users_data, file)
    with open('passwords.txt', 'w') as file:
        json.dump(password_data, file)
    print("Student added successfully")
    admin_panel()

def remove_student():
    """This function removes a student from the system."""
    print("Removing a student")
    users_data = load_data('users.txt')
    password_data = load_data('passwords.txt')
    grades_data = load_data('grades.txt')
    eca_data = load_data('eca.txt')
    user = input("Username:- ")
    for i in range(1, len(users_data) + 1):
        if user == users_data[f"{i}"]["user"]:
            users_data.pop(f"{i}") # pop le dictnory bata key remove garxa
            password_data.pop(f"{i}")
            grades_data.pop(f"{i}")
            eca_data.pop(f"{i}")
            with open('users.txt', 'w') as file:
                json.dump(users_data, file)
            with open('passwords.txt', 'w') as file:
                json.dump(password_data, file)
            print("Student removed successfully")
            admin_panel()
    else:
        print("Student not found")
        remove_student()

def view_students():
    """This function views all the students in the system."""
    print("Viewing all students")
    users_data = load_data('users.txt')
    for i in range(1, len(users_data) + 1):
        print(f"User: {users_data[f'{i}']['user']}, Role: {users_data[f'{i}']['role']}")
    admin_panel()
     

def exit():
    """This function exits the program."""
    print("Exiting the program")
    quit()

     

        



