import re

p = re.compile('^\d\d\d\w+(01|02|03|04|05|06|07|08|09|10|11|12|13|14|15|16)$')
print(p.match('777AAA02'))