from math import ceil, floor

std = [12, 20, 30, 36, 77, 10, 99, 3, 20]
N = len(std)
sum7 = 0
for i in range(0, N, 2):
    sum7 = sum7 + std[i]
N7 = ceil(N / 2)
avg7 = sum7 / N7
print("avg7 = " + str(avg7))
sum10 = 0
i = 1
for i in range(1, N, 2):
    sum10 = sum10 + std[i]
N10 = floor(N / 2)
avg10 = sum10 / N10
print("avg10 = " + str(avg10))

