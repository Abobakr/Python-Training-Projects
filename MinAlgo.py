# puan = [34, 56, 67, 12, 34, 52, 13, 67, 34, 23, 45, 78, 98, 45, 44]


N = int(input("Enter The count of numbers :"))
puan = [0]*N
i = 0
while i < N:
    puan[i] = int(input("Enter number " + str(i+1)+" : "))
    i = i + 1

min = puan[0]
N = len(puan)

i = 0
while i < N:
    if min > puan[i]:
        min = puan[i]
    i = i + 1

print('min = : '+ str(min))