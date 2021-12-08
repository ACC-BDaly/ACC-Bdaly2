file1 = open("C:/Users/17BDaly.acc/Downloads/10Random.txt", "r")
file2 = open("C:/Users/17BDaly.acc/Downloads/100Random.txt", "r")
# print(file1.read())
# print(file2.read())



# The range tells us how spread out a group of numbers are. To calculate the range
# we subtract the smallest number from the largest.
listEnd = []
list1 = file1.read()
'''print(type(list1))'''
for item in list1.split():
    listEnd.append(int(item))
listEnd.sort()
answer = listEnd[-1] - listEnd[0]
print('Range of 10: ', answer)

listEnd2 = []
list2 = file2.read()
'''print(type(list2))'''
for item in list2.split():
    listEnd2.append(int(item))
listEnd2.sort()
answer2 = listEnd2[-1] - listEnd2[0]
print('Range of 100: ', answer2)

print('\n')
# The frequency is a count of how often each different number appears
frequency = {}

for item in listEnd:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

print('List 10 Frequency', frequency)

'''\/ *www.tutorialspoint.com* \/'''

frequency2 = {}

for item in listEnd2:
   if item in frequency2:
      frequency2[item] += 1
   else:
      frequency2[item] = 1

print('List 100 Frequency', frequency2)

'''^^ *www.tutorialspoint.com* ^^'''

print('\n')

# The mean is the average of all the numbers. To calculate the mean, add all the numbers together and divide this value by the number of numbers
sumOflistEnd = sum(listEnd)
sumOflistEnd2 = sum(listEnd2)

meanlistEnd = sumOflistEnd / 10
meanlistEnd2 = sumOflistEnd2 / 100
print('Mean of 10: ', meanlistEnd)
print('Mean of 100: ', meanlistEnd2)

print('\n')

# The mode is the number which appears most often. If two numbers occur with the same frequency, the data is bi-modal, and more than two is multimodal
'''\/ * https://stackabuse.com/ * \/'''
import statistics
modeOFListEnd = statistics.mode(listEnd)
print('Mode of 10: ', modeOFListEnd)
modeOFListEnd2 = statistics.mode(listEnd2)
print('Mode of 100: ', modeOFListEnd2)
'''^^ * https://stackabuse.com/ * ^^'''

print('\n')

# The median is the number that is in the middle if you were to order all the numbers from largest to smallest.
medianOFListEnd = statistics.median(listEnd)
print('Median of 10: ', medianOFListEnd)
medianOFListEnd2 = statistics.median(listEnd2)
print('Median of 100 : ', medianOFListEnd2)

file3 = open("C:/Users/17BDaly.acc/Downloads/worksheet10.txt", "w")
file3.write('Range of 10 : ')
file3.write(str(answer))
file3.write('\n')
file3.write('Range of 100 : ')
file3.write(str(answer2))
file3.write('\n')
file3.write('Frequency of 10 : ')
file3.write(str(frequency))
file3.write('\n')
file3.write('Frequency of 100 : ')
file3.write(str(frequency2))
file3.write('\n')
file3.write('Mean of 10 : ')
file3.write(str(meanlistEnd))
file3.write('\n')
file3.write('Mean of 100 : ')
file3.write(str(meanlistEnd2))
file3.write('\n')
file3.write('Mode of 10 : ')
file3.write(str(modeOFListEnd))
file3.write('\n')
file3.write('Mode of 100 : ')
file3.write(str(modeOFListEnd2))
file3.write('\n')
file3.write('Median of 10 : ')
file3.write(str(medianOFListEnd))
file3.write('\n')
file3.write('Median of 100 : ')
file3.write(str(medianOFListEnd2))
file3.close()
'''
___________________________________________________________________________________________________________________________________________________________________'''
'''Example 1:
1,2,3,4,5,6,7,8,9,10,11 – here 6 is the median because it is in the middle of all the numbers ordered
from largest to smallest
1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11 – here 3 is the median because it is in the middle of all
the numbers ordered from largest to smallest

Example 2:
1,2,3,4,5,6,7,8,9,10 - here 5.5 is the median. If we have an even number of numbers, there is no
single “middle number”, so we add the middle two numbers together and divide them by 2
File – read input worksheet 26 November 2021
10Random.txt
Mean 64.3
Median 76
Mode 41
Range 73
100Random.txt
Mean 53.33
Median 55
Mode 50
Range 99'''