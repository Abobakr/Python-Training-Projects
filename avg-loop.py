std = [12, 20, 30, 36, 77, 10, 99, 3, 7]
N = len(std)
sum = 0
for i in range(N):
    sum = (sum + std[i])
avg = sum / N
print("avg = " + str(avg))
