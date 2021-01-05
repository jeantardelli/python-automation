"""
This module presents more of regex. It presents pattern elements and groups,
and shows how to retrieve and parse strings.
"""
import re

# Match a phone pattern as part of a group (in brakets)
match = re.search(r'the phone number is ([\d-]+)', '37: the phone number is '
                  '1234-567-890')
print(r'pattern: the phone number is ([\d-]+), string: 37: the phone number'
      ' is 1234-567-890\n{}\ngroup: {}\ngroup 1: {}\n'.format(match,
                                                              match.group(),
                                                              match.group(1)))

# Compile a pattern and capture a case-insensitive pattern
pattern = re.compile(r'The answer to question (\w+) is (yes|no)', re.IGNORECASE)
print('pattern: {}, string: Naturally, the answer to question 3b is YES'
        '\n{}\ngroups: {}\n'.format(pattern,
                                    pattern.search(
                        'Naturally, the answer to question 3b is YES'),
                                    pattern.search(
                        'Naturally, the answer to question 3b is YES').groups()))

# Match all the occurrences of cities and state abbreviations in text
pattern = re.compile(r'([A-Z][\w\s]+?).(TX|OR|OH|MI)')
text = '''the jackalopes are the team of Odessa,TX while the
knights are native of Corvallis OR and the mud hens come from
Toledo.OH; the whitecaps have their base in Grand Rapids,MI'''
cities_and_state_abbreviations = list(pattern.finditer(text))
print('pattern: {}\nstring: {}\nAll matches:'.format(pattern, text))
for i in cities_and_state_abbreviations:
    print(i)

# Naming a group
pattern = re.compile(r'(?P<city>[A-Z][\w\s]+?).(?P<state>TX|OR|OH|MN)')
match = pattern.search(text)
print('\npattern: {}'.format(pattern))
print('groupdict: {}'.format(match.groupdict()))
print('first city: {}'.format(match.group('city')))
print('first state: {}'.format(match.group('state')))
