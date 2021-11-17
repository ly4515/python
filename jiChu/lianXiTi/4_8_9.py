# 4_8
lifang = []
nums = range(1, 11)
for num in nums:
    lifang.append(num**3)
    #print(num**3)
print(lifang)

print("=============")

# 4_9 列表解析
lifang = [num**3 for num in range(1, 11)]
print(lifang)