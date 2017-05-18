import re

#@mail.com
#@gmail.com

p = re.compile('^\w+\.?\w+@(gmail\.com|mail\.ru|yandex\.ru|icloud\.com)$')
print(p.match('yeldan.s@yandex.ru'))

