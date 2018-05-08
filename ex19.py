#this line creates a function called cheese and crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#this line prints out the number of cheeses you have using the format string method
    print 'You have {0} cheeses!'.format(cheese_count)
#this line prints out the number of boxes of crackers using the format string methode
    print 'You have {0} boxes of crackers!!'.format(boxes_of_crackers)
#this line prints out a statement
    print 'Man that\'s enough for a party!'
#this line print s out another statement
    print 'Get a blanket.\n'

print 'We can just give the function numbers directly:'

#this line calls the function and then gives it two arguments
cheese_and_crackers(20,30)
pri
print 'OR, we can use variables from our script:'
#this line says that when you pass a function arguments you can also pass it variables
amount_of_crackers = 10
#make variable
amount_of_cheese = 50
#make variable
cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#print the statement that we can do math inside the parameters as well
print 'We can even do math inside too:'
cheese_and_crackers(10+20, 5+6)
#print the statement that we can do math inside the parameters and math on the parameters as well
print 'And we can combine the two, variables and math:'
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)
