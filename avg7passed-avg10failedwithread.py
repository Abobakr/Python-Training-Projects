N = int(input("enter number of students : "))
while N < 1:
    print("Not a valid number.\nPlease enter another number")
    N = int(input())
print("enter degrees one by one")
std = [0] * N
for i in range(N):
    good_input = False
    while not (good_input):
        try:
            under_test = int(input())
            if 0 <= under_test <= 100:
                good_input = True
                std[i]=under_test
            else:
                print("please enter a degree between 0 and 100")
        except:
            print("Not a valid input. Please enter number")
print("students degrees ", std)
sum7 = 0
N7 = 0
for i in range(0, N, 2):
    if std[i] >= 18:
        sum7 = sum7 + std[i]
        N7 = N7 + 1
if N7 == 0:
    print("no successful 7th grade students")
else:
    avg7 = sum7 / N7
    print("successful avg7 = " + str(avg7))
sum10 = 0
N10 = 0
for i in range(1, N, 2):
    if std[i] < 28:
        sum10 = sum10 + std[i]
        N10 = N10 + 1
if N10 == 0:
    print("no failed 10th grade students")
else:
    avg10 = sum10 / N10
    print(" failed avg10 = " + str(avg10))
