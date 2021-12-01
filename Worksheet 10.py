file1 = open("C:/Users/17BDaly.acc/Downloads/10Random.txt", "r")
file2 = open("C:/Users/17BDaly.acc/Downloads/100Random.txt", "r")
print(file1.read())
print(file2.read())

# The range tells us how spread out a group of numbers are. To calculate the range we subtract the
# smallest number from the largest.
# The frequency is a count of how often each different number appears
# The mean is the average of all the numbers. To calculate the mean, add all the numbers together
# and divide this value by the number of numbers
# The mode is the number which appears most often. If two numbers occur with the same frequency,
# the data is bi-modal, and more than two is multimodal
# The median is the number that is in the middle if you were to order all the numbers from largest to
# smallest.
# Example 1:
# 1,2,3,4,5,6,7,8,9,10,11 – here 6 is the median because it is in the middle of all the numbers ordered
# from largest to smallest
# 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11 – here 3 is the median because it is in the middle of all
# the numbers ordered from largest to smallest
# Example 2:
# 1,2,3,4,5,6,7,8,9,10 - here 5.5 is the median. If we have an even number of numbers, there is no
# single “middle number”, so we add the middle two numbers together and divide them by 2
# File – read input worksheet 26 November 2021
# 10Random.txt
# Mean 64.3
# Median 76
# Mode 41
# Range 73
# 100Random.txt
# Mean 53.33
# Median 55
# Mode 50
# Range 99