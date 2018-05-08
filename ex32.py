the_count = [1, 2, 3, 4]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop gpes through a CHECKLIST
# for number in the_count:
#     print 'this is count {}' number
for number in the_count:
    print ('this is the count of {}.'.format(number))
#sames as above
for fruit in fruits:
    print ('this is the pinche\' {} fruit ok guapoooo??'.format(fruit))

for item in change:
    print ('this is a mixed list loop, see? {}'.format(item))

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 20 counts
for i in range (0, 6):
    print ('Adding {} to the list'.format(i))
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print ('Elements was: {}'.format(i))

print (elements)


#EC

elements =[]
elements.extend(range(0,6))
print('QA check on loop:', elements)
