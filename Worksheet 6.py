for (n) in range (1,11):
    print(n)

#2
for (n) in range (1,11):
    nums=(range(10,21,2))
print(sum(nums))

#3
for num in range(20,1,-2):
    print(num)

#4
for num in range (1,11):
    print(num**2, num**3)
    
#5
numbers=int(input("Number: "))
for number0 in range(numbers + 1):
    for j in range(number0):
        print("*", end=" ")
    print(" ")
    

#7
numbers = []
for number0 in range(5):
    numbers.append(int(input("Number: ")))
answer = 1
for j in numbers:
    answer *= j
print(answer)    
    
     