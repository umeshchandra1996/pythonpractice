import os
import sys
import random
super_villains={'Fidder' : 'Isaac Bowin',
                'Captain Cold' : 'Leonard Snart',
                'Weather Wizard' : 'Mark Mardon',
                'Mirror Moster' : 'Sam Scudder',
                'Pied Piper' : 'Thomas petreson'
                }

print(super_villains.get('Mirror Moster'))#given key for value
print(super_villains.get ("Thomas petreson"))#its none bcz Thomas petreson is not key
       
print(super_villains.keys())

print(super_villains.values())

print(super_villains.items())#its provied all element and value


