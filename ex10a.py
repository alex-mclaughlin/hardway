print "I am 6'2\" tall."
print 'I am 6\'2" tall.'
tabby_cat = "\tI'm tabbed in. "
persian_cat = "I'm split\non a line."
backlash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backlash_cat
print fat_cat

egyptian_cat = "%r is a member of the \"Cats\" Club."
print egyptian_cat % ("Alex")
