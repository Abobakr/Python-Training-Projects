student = [100, 88, 29,47, 59, 30, 47, 66,85, 90, 30, 46, 20, 40 , 10]
N = len(student)
max = student[0]
i = 0
while i < N:
    if max < student[i]:
        max = student[i]
    i = i + 1
min = student[0]
i = 0
while i < N:
    if min > student[i]:
        min = student[i]
    i = i + 1
range = max - min
print("range = " + str(range))
