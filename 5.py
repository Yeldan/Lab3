import re

p = re.compile('^(A|B|C|D|E|F|H|K|L|M|N|O|P|R|S|T|U|V|W|X|Z) \d\d\d \w+$')
print(p.match('A 777 AAA'))