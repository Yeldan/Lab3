import re

p = re.compile('^((7|\+7|8|)( |-)?(727|717)( |-)?)?(2|3)( |-)?\d\d( |-)?\d\d( |-)?\d\d$')
print(p.match('3675887'))