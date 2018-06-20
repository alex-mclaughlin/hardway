cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = 'New York'
cities['OR'] = 'Portland'
cities['MN'] = 'JAYFREAKINGMAINE'
cities['UT'] = 'Salt Lake City'
print cities
def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not Found."

#test
cities['_find'] = find_city

while True:
    print ("State? (ENTER to quit)")
    state = raw_input("> ")

    if not state: break

    city_found = cities['_find'](cities, state)
    print (city_found)


# #EC
# #cities = ['San Francisco', 'Detroit', 'Jacksonville']
# cities = ['San Francisco', 'Detroit', 'Jacksonville', 'Salt Lake', 'Topeka']
# for city in cities:
#     if cities.index(city) > 3:
#         print city,':',cities.index(city)
