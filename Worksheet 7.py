'''import time'''

string = 'Hello There Bob'
'''print(len(string))'''

'''time.sleep(1)
print(string[0])

time.sleep(1)
print(string[4])

time.sleep(1)
print(string[14])

for ch in string:
 print(ch)

for ch in range(0,len(string)):
 print(string[ch])

for ch in range(0,len(string)):
 print(ch)

time.sleep(2)

print(string.upper()) #returns uppercase string
print(string.lower()) #returns lowercase string
print(string.count('e')) #counts how many times x appears
print(string.find('e')) #position of the first occurrence of x
print(string.replace('e','b')) #replaces x with y
print(string.islower()) #returns True if all characters are lowercase
print(string.isupper()) #returns True if all characters are uppercase
print(string.isalnum()) #returns True if all characters are alphanumeric
print(string.isalpha()) #returns True if all characters are alphabetic
print(string.isdigit()) #returns True if all characters are digits
print(string.index('e')) #returns index of substring s in string
print(string.strip('e')) #returns a string with leading and trailing characters removed
'''


#string[0] = ‘W’
#Strings are immutable

userWord = str(input('Give me a word : '))
userWord = userWord.lower()
wordcounter = 1
for check in range(0,(len(userWord)//2)-1):
    if userWord[check] != userWord[-(check+1)]:
        print(userWord, 'Your word is not a palindrome')
    else:
       print(userWord, 'Your word is a palindrome')

