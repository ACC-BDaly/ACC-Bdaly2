"""#1
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

#6 WORK IN PROGRESS
electricityUnit = int(input("Please Enter Your Energy Used : "))
if electricityUnit < 100:
    print("Amount Due : €", electricityUnit * 0)

if electricityUnit > 100:
    remainderUnit = electricityUnit - 100
    print("Amount Due : €",remainderUnit * 0.05)

if 100 < electricityUnit > 200:
    remainderUnit = electricityUnit - 100
    
    hundredUnits = 100 * 0.05
    endRemainder = remainderUnit + hundredUnits
    print("Amount Due : €",remainderUnit * 0.10)

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
if dayNumber == 1:
    print ("Monday")
if dayNumber == 2:
    print ("Tuesday")
if dayNumber == 3:
    print ("Wednesday")
if dayNumber == 4:
    print ("Thursday")
if dayNumber == 5:
    print ("Friday")
if dayNumber == 6:
    print ("Saturday")
if dayNumber == 7:
    print ("Sunday")

#10
tempCent = float(input("Enter the temperature: "))
equation = (9 / 5 * tempCent) + 32
tempFahr = round(equation, 2)
print(tempFahr)
"""
#11
day = int(input("Enter the date: "))
month = input("Enter the month: ")
year = int(input("Enter the year: "))
