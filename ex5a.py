name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
shoe_size = 13


print 'Let\'s talk about {0}'.format(name)
print 'He\'s {0} inches tall.'.format(height)
print 'He\'s {0} pounds heavy.'.format(weight)
print 'Actually that\'s not too heavy.'
print 'He\'s got {0} eyes and {1} hair.'.format(eyes, hair)
print 'His teeth are usually {0} depending on the coffee.'.format(teeth)

#this line is tricky, try to get it exactly right
print 'If I add {}, {}, and {} I get {}.'.format(age, height, weight, age + height + weight)
print 'And this is my shoe size = {}'.format(shoe_size)
