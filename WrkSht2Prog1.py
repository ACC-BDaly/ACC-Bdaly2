#1
print('*Please enter a number!*')
firstNumber = float(input('Number 1 :'))
import time
time.sleep(2)
print('*Please enter another number!*')
secondNumber = float(input('Number 2 :'))
numbers = [firstNumber, secondNumber]
sorted(numbers)
print(sorted(numbers))

#2
print('*Please enter your age!*')
userAge = int(input('Age : '))
if userAge < 17:
    print("You are INELIGIBLE to vote!")
else:
    print("You are ELIGIBLE to Vote")

#3
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

#4
userNumber = float(input("Type a number : "))
if (userNumber % 7) == 0:
   print("{0} is divisible by 7".format(userNumber))
else:
   print("{0} is not divisible by 7".format(userNumber))

#5
userNumber = float(input("Type a number : "))
if (userNumber % 5) == 0:
   print("Hello".format(userNumber))
else:
   print("Bye".format(userNumber))

#6

#7
threeDigitNumber = int(input("Enter a three digit number: "))
last_digit = threeDigitNumber % 10
print(last_digit, "is the last digit")

#8
threeDigitNumber = int(input("Enter a three digit number: "))
last_digit = threeDigitNumber % 10
if (last_digit % 3) == 0:
    print(last_digit, "is divisible by 3")
else:
    print(last_digit, "is not divisible by 3")


#9
dayNumber = int(input("Enter a number between 1-7: "))
if (dayNumber == 1)