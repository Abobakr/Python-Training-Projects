import math

std = [50, 40, 80, 90, 70]
i = 0
N = len(std)
sum = 0
while i < N:
    sum = sum + std[i]
    i = i + 1
avg = sum / N
i = 0
stdsquare = [0] * N
while i < N:
    stdsquare[i] = math.pow(std[i] - avg,2)
    i = i + 1
i = 0
sum = 0
while i < N:
    sum = sum + stdsquare[i]
    i = i + 1
variance = sum / (N - 1)
sd = math.sqrt(variance)
print("sd = " + str(sd))
