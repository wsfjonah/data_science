import re


str = 'abc21#@23'

result = re.sub('[\D_]+', '', str)

print(result)