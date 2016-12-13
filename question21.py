#! python3
# This file is the code I wrote to answer practice problem 21 in Automate The Boring Stuff: Chapter 7

import re

testString = ['Satoshi Nakamoto',
              'Alice Nakamoto',
              'Robocop Nakamoto',
              'satoshi Nakamoto',
              'Mr. Nakamoto',
              'Nakamoto',
              'Satoshi nakamoto']

nameRegex = re.compile(r'(^[A-Z][a-z]*)\sNakamoto')

for item in testString:
    mo = nameRegex.search(item)
    if mo is None:
        result = 'Nothing'
    else:
        result = mo.group()
    print('{} found in string {}'.format(result, item))
