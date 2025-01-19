std = [10, 90, 80, 60, 40, 20, 45, 55, 70, 66, 34, 20, 50]
N = len(std)
sum = 0
for i in range(N):
    sum = sum + std[i]
print("sum = " + str(sum))
