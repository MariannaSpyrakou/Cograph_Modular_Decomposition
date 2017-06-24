from create_cotree import create_cotree

d = {'a': ['b','d','e','f','x'],
         'b': ['a','f','e','d'], 'c': ['f','e','d'],
         'd': ['a','b','c','x'], 'e': ['a','b','c','x'],
         'f': ['a','b','c','x'] , 'x': ['f','a','d','e']
         }
create_cotree(d)
