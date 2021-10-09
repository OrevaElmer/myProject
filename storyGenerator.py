#This program generate a story:

import random

when = ['Last night','Yesterday','A long time ago']
what = ['a goat','a rat','a rabbit','a zebra']
name = ['James','Jeffery','Isaiah','Cook']
location = ['America','Africa','Asia','Europe']

def choices(value):
    return random.choice(value)

myStory = f"{choices(when)}, {choices(what)} named \
{choices(name)}, travelled to {choices(location)}"

print(myStory)