std=[25, 30, 15, 26, 35, 29, 24, 15]
N=len(std)
sum7=0
N7=0
for i in range(0, N, 2):
    if std[i]>=18:
        sum7=sum7+std[i]
        N7=N7+1
if N7==0:
    print("no successful 7th grade students")
else:
    avg7 = sum7 / N7
    print("successful avg7 = " + str(avg7))
sum10=0
N10=0
for i in range(1, N, 2):
    if std[i]<28:
        sum10=sum10+std[i]
        N10=N10+1
if  N10==0:
    print("no successful 10th grade students")
else:
    avg10 = sum10 / N10
    print(" failed avg10 = " + str(avg10))
print("50->60", list( range (30, 71, 5)))