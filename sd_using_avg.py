def sumALGO(nums):
    N = len(nums)
    sigma = 0
    i = 0
    while i < N:
        sigma = (sigma + nums[i])
        i = i + 1
    return sigma


def avgALGO(nums):
    N = len(nums)
    sum = sumALGO(std)
    avg = sum / N
    return avg


def sqaured_difsALGO(nums, avg):
    N = len(nums)
    sqaured_difs = [0] * N

    i = 0
    while i < N:
        sqaured_difs[i] = (nums[i] - avg) ** 2
        i = i + 1

    return sqaured_difs


def sdALGO(sayilar):
    ortalama = avgALGO(sayilar)
    sqaured_difs = sqaured_difsALGO(avg= ortalama,nums=sayilar)
    variance = avgALGO(sqaured_difs)
    sd = variance ** 0.5
    return sd


std = [12, 20, 30, 36, 77, 10, 99, 3, 7]
sd = sdALGO(std)
print("sd : " + str(sd))
