
def sumALGO(nums):
    N = len(nums)
    sigma = 0
    i = 0
    while i < N:
        sigma = (sigma + nums[i])
        i = i + 1
    return sigma


std = [12, 20, 30, 36, 77, 10, 99, 3, 7]
N = len(std)
sum =sumALGO(std)
avg = sum / N
print("avg = " + str(avg))
