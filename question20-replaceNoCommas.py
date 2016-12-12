# This is the code in answer to the practice problem number 20 in Automate The Boring Stuff Chapter 7.

import re

numRegex = re.compile(r'''^(
    ^(\d){1,3}              # 1 to 3 leading digits. This group would be required. Accounts for matches < 1000
    (,?(\d){3})*             # second group would have to START with a comma

    )$''', re.VERBOSE)

commaRegex = re.compile(r',')

stringList = ['42', '1,234', '6,368,745', '12,34,567', '1234', '65432']

newString = []

for item in stringList:
    mo = numRegex.search(item)
    if mo is None:
        result = 'Nothing'
    else:
        result = mo.group()
    print('{} found in string {}'.format(result, item))
    result = commaRegex.sub('', result)
    newString.append(result)
print(newString)

print('Hello World!')
