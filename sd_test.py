from math import sqrt


def sdALGO(numbers):
    avg = avgALGO(numbers)
    differences = sqaured_difsALGO(numbers, avg)
    difsAvg = avgALGO(differences)
    sd = sqrt(difsAvg)
    return sd


def avgALGO(numbers):
    N = len(numbers)
    sum = sumALGO(numbers)
    avg = sum / N
    return avg


def sumALGO(numbers):
    N = len(numbers)
    sum = 0
    i = 0
    while i < N:
        sum = sum + numbers[i]
        i = i + 1
    return sum


def sqaured_difsALGO(numbers, avg):
    N = len(numbers)
    squared_difs = [0] * N
    i = 0
    while i < N:
        squared_difs[i] = (numbers[i] - avg) ** 2
        i = i + 1
    return squared_difs


std=[50,60, 70 ]
print("sd = " , sdALGO(std))