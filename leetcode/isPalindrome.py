class Solution:
    def isPalindrome(x):
        return str(x)[ : : -1] == str(x)

print(Solution.isPalindrome(909))



"""
https://www.liaoxuefeng.com/wiki/1016959663602400/1017269965565856
切片思想

所有数，每5个取一个：
>>> L[::5]



"""