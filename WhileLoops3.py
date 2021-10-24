
#1
print('Please enter 10 numbers : ')
totalNumber = 0
counter = 0
while counter < 10:
    totalNumber = totalNumber + float(input('Enter Number :'))
    counter = counter + 1
endNumber = totalNumber / 10
print(endNumber)
#2
totalNumber = 24
counter = 0
while counter <= 12:
    counter += 1
    print(counter * totalNumber)
#3
n = 1
while n > 0:
    n -= 0
    print('Infinite to the screen')

#4
n=""
while type(n)!= int:
    try:
        n = int(input('Enter a number to find its factorial: '))
    except ValueError:
        print('This isnt an integer!')
        pass
multiply = 1
total = 1
while multiply <= n:
    total = total * multiply
    multiply += 1 
print('factorial = ', total)

#5
noOne = int(input('Enter a number :'))
noTwo = int(input('Enter a number :'))

remainder = int
while remainder != 0:
    result = noOne // noTwo
    remainder = noOne % noTwo
    noOne = noTwo
    noTwo = remainder
print(noOne, 'is the Highest Common Factor')

#6
decimal = float(input('Enter a number to be converted to binary : '))
binary = ''

while decimal != 0:
    binary  = str(decimal % 2) + binary 
    decimal //= 2

print (binary)