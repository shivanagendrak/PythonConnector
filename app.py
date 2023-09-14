import sys
from databasehelper import DBhelper
class Amazon:
    def __init__(self):
        self.db = DBhelper() # connecting to database part
        self.menu()
    def login_menu(self):
         user_input = input("""                       
Enter 1 to see profile
Enter 2 to edit profile
Enter 3 to delete profile                            
                         """)
         if user_input == "1"or"2" or"3" :
              print("Not yet built")
         else:
              print("Not yet built")
    def menu(self):
        user_input = input("""
1. Enter "1" to Register
2. Enter "2" to Login
3. Enter "3" or Anynumber to Exit
""")
        if user_input == "1":
            self.register()
        elif user_input == "2":
            self.login()
        else:
            sys.exit(1000)
    def register(self):
        name = input("Enter your Name:")
        email = input("Enter your Email:")
        password = input("Enter your Password:")

        response = self.db.register(name,email,password)

        if response:
            print("Success")
        else:
            print("Error")
        self.menu()
    def login(self):
        email = input("Enter your Email:")
        password = input("Enter Your Password:")
        data = self.db.search(email,password)
        print("Hello",data[0][1])
        if len(data)==0:
                print("Incorrect email/password")
        else:
                print("Hello",data[0][1])
                self.login_menu()
         
        
obj = Amazon()