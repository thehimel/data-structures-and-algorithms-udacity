"""
You're going to work on a dictionary that stores cities
by country and continent. The following one is done for you
- the city of Mountain View is in the USA, which is in North America.

locations = {'North America': {'USA': ['Mountain View']}}

Notice that:
locations is a dictionary of dictionaries
North America (Continent) is a dictionary
USA (Country) is a key
['Mountain View'] (City) is a list acting as a value.
A new city within USA country can be "appended" to the given list.

Task 1
------
You need to add the cities listed below by modifying the given structure.
Cities to add:
Bangalore (India, Asia)
New Delhi (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)

Be careful, while adding a city in an existing country.
Consider adding it to the existing list of cities as:

locations['Asia']['India'].append('New Delhi')

Task 2
------
Print the following (using "print") by looking them up in the structure.

A list of all cities in the USA in alphabetic order.
All cities in Asia, in alphabetic order, next to the name of the country.
In your output, label each answer with a number so it looks like this:

1
American City
American City

2
Asian City - Country
Asian City - Country
"""


# Task 1 - Solution
locations = {'North America': {'USA': ['Mountain View']}}
locations['North America']['USA'].append('Atlanta')
locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['Asia']['China'] = ['Shanghai']
locations['Africa'] = {'Egypt': ['Cairo']}

# Task 2 - Solution
# Part 1 - A list of all cities in the USA in alphabetic order.
print(1)
usa_sorted = sorted(locations['North America']['USA'])
for city in usa_sorted:
    print(city)

# Part 2 - All cities in Asia, in alphabetic order
print(2)
asia_cities = []
for country, cities in locations['Asia'].items():
    for city in cities:
        asia_cities.append('{} - {}'.format(city, country))
asia_sorted = sorted(asia_cities)
for city in asia_sorted:
    print(city)
