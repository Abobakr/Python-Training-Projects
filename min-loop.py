student=[12, 20, 30 , 36, 77, 10, 99,3, 7 ]
N=len(student)
min=student[0]
i=0
while i<N:
    if min>student[i]:
        min=student[i]
    i=i+1
print("min = " + str(min))