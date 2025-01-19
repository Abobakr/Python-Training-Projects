# Ex = [1002, 12, 34, 1000, 78, 88, 1001]
# maxi = Ex[0]
# N = len(Ex)
# for i in range(1, N):
#     if maxi < Ex[i]:
#         maxi = Ex[i]
# print(maxi)
nums = [12, 354, 76, 8, 0, 40]
sigma = 0
i = 0
n = len(nums)
while i < n:
    sigma = sigma + nums[i]
    i = i + 1
print('sum = ' + str(sigma))
