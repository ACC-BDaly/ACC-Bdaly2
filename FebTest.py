L =[23,1,0,-12,48, 15, 9, 20, -11, 42,7, -5, 13]
#Program 1: Write a program to print the sum of every second number in the list L

'''sum1 = sum(L[1:2]+L[3:4]+L[5:6]+L[7:8]+L[9:10]+L[11:12]+L[13:0])
print(sum1)'''

#Program 2: Write a program to print the product of all the numbers in the list L



#Program 3: Write a program to print every number between 0 and 10000 inclusive

'''for i in range (0, 10001):
    print(i)'''

#Program 4: Write a program to print all the characters in the string ‘CodeHappy’ on a separate line

'''words = "Code Happy"
for i in words:
    print(i, sep='\n')'''

#Program 5: Write a program to take in the length and width of a rectangle and print its area

'''userInputLength = float(input("Input Length : "))
userInputWidth = float(input("Input Width : "))
area = userInputLength*userInputWidth
print(area)'''

#Program 6: Write a program that repeatedly asks the user to enter some text and only stops if the user enters the character ‘z’ or ‘Z’

'''userInput = ""
while userInput != "z":
    userInput = input("type something").lower()'''

#Program 7: Write a program to open a file called ‘CS04022022.txt’ and print the poem below to the file before closing it–the lines should be as below, not in one long line in the file

'''f = open('CS0402202.txt', 'w')
f.write('Leunig – How To Get There')
f.write('\n')
f.write('\n')
f.write('Go to the end of the path until you get to the gate.')
f.write('\n')
f.write('Go through the gate and head straight out towards the horizon.')
f.write('Keep going towards the horizon.')
f.write('\n')
f.write('Sit down and have a rest every now and again,')
f.write('\n')
f.write('But keep on going, just keep on with it.')
f.write('\n')
f.write('Keep on going as far as you can.')
f.write('\n')
f.write('That is how you get there.')
f.close()'''