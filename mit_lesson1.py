# n = 0
# while n < 5:
#     print n
#     n = n + 1
# for n in range(5):
#     print(n)

# x = 5
# if x !5:
#     print('i am here')
# else:
#     print('no I am not')

# x = float(input('Enter a number for x:  '))
# y = float(input('Enter a number for y:  '))
# if x == y:
#     print('X and Y are equal')
#     if y!= 0:
#         print ('therefore, x /y is', x/y)
# elif x < y:
#     print('x is smaller than y')
# else:
#     print('y is smaller')
# print('thanks')


# if x%2 == 0:
#     print('')
#     print('Even')
# else:
#     print('')
#     print('Odd')
# print('Done')

# branching programs
#  has a conditional
#  A test (expression that evaluates to True or False)
#  A block of code to execute if the test is True
#  an optional block of code to execute if the test is False

# Using control in Loops
#     want to do things over and over again


# n = input("You are in the Lost Forest. Go left or right?")
# while n == 'right':
#     n = input("You are ing the Lost Forest. Go left or right")
# print ("you got out of the lost forest!")
#
# n = 0
# while n < 5:
#     print(n)
#     n = n + 1
# x = 3
# ans = 0
# intersLeft = x
# while (intersLeft != 0):
#     ans = ans + x
#     intersLeft = intersLeft -1
# print(str(x) + '*' + str(x) + ' = ' + str(ans))
#
# happy = 0
# while happy < 2:
#     happy = happy + 1
# print('hello world')

# varA = "print me"
# # varA = 1
# varB = 10
# if type(varA) == str or type(varB) == str:
#     print("string involved")
# elif varA > varB:
#     print("bigger")
# elif varA == varB:
#     print("equal")
# elif varA < varB:
#     print("smaller")


# mysum = 0
# for i in range(5,11, 2):
#     mysum += i
# print(mysum)

# num = 0
# while num <= 5:
#     print(num)
#     num += 1
#
# print("Outside of loop")
# print(num)

# numberOfLoops = 0
# numberOfApples = 2
# while numberOfLoops < 10:
#     numberOfApples *= 2
#     numberOfApples += numberOfLoops
#     numberOfLoops -= 1
# print("Number of apples: " + str(numberOfApples))

# num = 10
# while True:
#     if num < 7:
#         print('Breaking out of loop')
#         break
#     print(num)
#     num -= 1
# print('Outside of loop')

# x = 2
# while x <= 10:
#     print(x)
#     x = x + 2
# print('Goodbye!')

# print ('Hello!')
# x = 10
# while x > 0:
#     print (x)
#     x = x - 2
#
# total = 0
# num = 1
# while num <= end:
#     total += num
#     num += 1
#print(total)

# total = 0
# end = 6
# for x in range(1, end):
#     #print (end)
#     #print(x)
#     total += end
#     #total += x
#     #total += total
# print(total)

# end = 6
# for i in range(end):
#     end += i
#
# print(end)
#
# 6+0+1+2+3+4+5

# print("Hello!")
# for x in range(10, 0, -2):
#     print(x)




# x = 5
#
# ans = 0
#
# intersLeft = x
#
# while (intersLeft != 0):
#     ans = ans + x
#     intersLeft = intersLeft - 1
# print(str(x) + '*' + str(x) + '=' + str(ans))


# num = 10
# for num in range(5):
#     print(num)
# print(num)
#
# divisor = 2
# for num in range(0, 10, 2):
#     print(num/divisor)

# for variable in range(20):
#     if variable % 4 == 0:
#         print(variable)
#     if variable % 16 == 0:
#         print('Foo!')

# count = 0
# for letter in 'Snow!':
#     print('Letter # ' + str(count) + ' is ' + str(letter))
#     count += 1
#     break
# print(count)

# greeting = 'Hello'
# count = 0
#
# for letter in greeting:
#     count += 1
#     if count % 2 == 0:
#         print(letter)
#     print(letter)
#
# print('done')
#
# #h,e,e,l,l,l,0,!,!

# school = 'Massachusetts Institute of Technology'
# numVowels = 0
# numCons = 0
#
# for char in school:
#     if char == 'a' or char == 'e' or char == 'i' \
#         or char == 'o' or char == 'u':
#             numVowels += 1
#     elif char == 'o' or char == 'M':
#         print(char)
#     else:
#         numCons -= 1
#
# print('numVowels is: ' + str(numVowels))
# print('numCons is: ' + str(numCons))

s = "azcbobobegghakl"
bobCount=0

for num in range(len(s)):
    if s[num:num+3] == "bob":
        bobCount += 1

print ("Number of time bob occurs is:",bobCount)




s = "azcbobobegghakl"

alphaCount = 0


print ("Longest
for num in
# x = int(x=input('Enter and interger: '))
#
# ans = 0
# while ans ** 3 < abs(x):
#     ans = ans + 1
# if ans** 3 != abs(x):
#     print(str(x) + ' is not a perfect cube')
# else:
#     if x < 0:
#             ans = - ans
#     print('Cube root of ' + str(x) + ' is ' + str(ans))

# iteration = 0
# count = 0
# while iteration < 5:
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1

# for iteration in range(5):
#     count = 0
#     while True:
#         for letter in "hello, world":
#             count += 1
#         print("Iteration " + str(iteration) + "; count is: " + str(count))
#         break

# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     while True:
#         count += len(phrase)
#         break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))


# count = 0
# phrase = "hello, world"
# for iteration in range(5):
#     count += len(phrase)
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
