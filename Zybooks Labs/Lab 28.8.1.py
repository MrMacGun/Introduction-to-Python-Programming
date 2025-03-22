#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/8

uint = input()
nums = list(map(float, uint.split()))

max_value = max(nums)

for num in nums:
    normalized_value = num / max_value
    print(f"{normalized_value:.2f}", end=" ")

print("")