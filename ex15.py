#this line imports the module argv from the sys library
from sys import argv

#this line tells argv varialbe to accept two arguements - the ex15.py and ex15_sample.txt
script, filename = argv

#this line opens the filename ex15_sample.txt and assigns that open file to the variable tx
#txt = open('ex15_sample.txt')

#the next two lines print the filename using the system argument filename
print "Here's your file %r:" % filename
#this line prints the contents of the text file
#print txt.read()

#this line prints a question to the user
#print "I'll also ask you to type it again:"
#this line takes the filename from the user and assigns it ot filename_again
#file_again = raw_input("> ")
#this line opens the text file and assigns this to txt_again

#txt_again = open('ex15_sample.txt')
#this line takes the users input of the filename that is opened in the line before
#and then prints the txt_again.read()
#print txt_again.read()

#txt.close()
#txt_again.close()
#You give a file a command (methods, functions) by using the . (dot or period),
#the name of the command, and parameters. Just like with open and raw_input.
#The difference is that when you say txt.read() you are saying,
#“Hey txt! Do your read command with no parameters!”
