#https://learn.zybooks.com/zybook/WGUD335Pythonv1/chapter/28/section/7


def get_user_values(nums):
    while True:
        value = int(input())
        if value == -1:
            break
        nums.append(value) 

def output_ints_less_than_or_equal_to_threshold(nums, threshold):
    for num in nums:
        if num <= threshold:
            print(num)

if __name__ == '__main__':
    threshold = int(input())
    nums = []
    
    get_user_values(nums)
    output_ints_less_than_or_equal_to_threshold(nums, threshold)
