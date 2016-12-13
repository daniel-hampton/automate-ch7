#! python3
# This code is to answer practice problem 22 in Automate the Boring Stuff: Chapter 7

import re

testStrings = ['Alice eats apples.',
               'Bob pets cats.',
               'Carol throws baseballs.',
               'Alice throws Apples.',
               'BOB EATS CATS',
               'Robocop eats apples.',
               'ALICE THROWS FOOTBALLS.',
               'Carol eats 7 cats.']

'''
Criteria for regex:
First word Alice, Bob, or Carol
Second word either eats, pets, throws
Third word is apples, cats, or baseballs
Sentence ends with period.
Case insensitive.
'''
sentenceRegex = re.compile(r'^(alice|bob|carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.$',
                           re.IGNORECASE)

for item in testStrings:
    mo = sentenceRegex.search(item)
    if mo is None:
        result = 'Nothing'
    else:
        result = mo.group()
    print('{} found in string {}'.format(result, item))
