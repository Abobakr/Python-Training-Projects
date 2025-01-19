# اكتب برنامج بلغة البايثون يقرأ الاسم وكلمة المرور من المستخدم  فإذا كان الاسم = "user1" والرمز السري = "1234" فإنه يرسل رسالة إلى المستخدم تظهر فيها "VALID LOGIN"
# (تسجيل دخول صالح) والا يستمر بطلب الاسم وكلمة المرور من المستخدم

user_name = input("Enter user name: ")
password = input("Enter password: ")
# Check if the grade is within the valid range
while user_name != 'user1' or password != "1234":
    print("Invalid user name or password, please RE-enter valid information: ")
    user_name = input("Enter user name: ")
    password = input("Enter password: ")

print("VALID LOGIN")
