from math import ceil, floor

std = [60, 50, 80, 40, 30, 20]
N = len(std)
sum7 = 0
N7 = 0
i = 0
while i < N:
    if std[i] >= 50:
        sum7 = sum7 + std[i]
        N7 = N7 + 1
    i = i + 2
if N7==0:
    print("no successful 7th grade students")
else:
    avg7 = sum7 / N7
    print("successful avg7 = " + str(avg7))
sum10 = 0
i = 1
N10 = 0
while i < N:
    if std[i] >= 60:
        sum10 = sum10 + std[i]
        N10 = N10 + 1
    i = i + 2
if  N10==0:
    print("no successful 10th grade students")
else:
    avg10 = sum10 / N10
    print(" successful avg10 = " + str(avg10))
