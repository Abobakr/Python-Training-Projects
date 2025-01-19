user_name = input("Enter user name: ")
password = input("Enter password: ")
# Check if the grade is within the valid range
while user_name != 'user1' or password != "1234":
    print("Invalid user name or password, please RE-enter valid information: ")
    user_name = input("Enter user name: ")
    password = input("Enter password: ")

print("VALID LOGIN")