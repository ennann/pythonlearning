def max_num():
    """
    Find the largest number in a list.
    """
    nums = [1, 2, 3, 4, 5]
    max_num = nums[0]
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


"""
Find the largest number in a list.
"""

t = max(1, 2, 3, 4, 5)
print(t)
