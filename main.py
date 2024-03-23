from functions import *
import time
def main():
    while True:
        user = input("Username:- ")
        pwd = input("Password:- ")
        creds,role = check_info(user, pwd)
        time.sleep(3)
        if creds:
            print("Access granted")
            if role == "admin":
                admin_panel()
                break
            else:
                student_panel(user,pwd)
                break
        else:
            print("Access denied! Try again !")



if __name__ == "__main__":
    main()