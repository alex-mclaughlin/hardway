from sys import argv
from os.path import exists

#from_file, to_file = argv[1:]
#print 'Copying from {0} to {1}'.format(from_file, to_file)



#we could do these two on one line too, how?
open(argv[1], 'wb').write(open(argv[2], 'r').read().close()).close()
# indata = open(from_file).read()
#
# # with open(from_file) as in_file:
# #     indata = in_file.read()
#
# #print "The input file is {0} bytes long".format(len(indata))
#
# #print "Does the output file exist? {0}".format(exists(to_file))
# #print "Ready, hit RETURN to continue, CTRL-C to abort."
# #raw_input()
#
# output = open(to_file, 'w')
# output.write(indata)
#
# print 'Alright, all done.'
#
# output.close()
