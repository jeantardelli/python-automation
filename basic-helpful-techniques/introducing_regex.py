"""
This module illustrates some pattern matches with regex module
"""
import re

# Match a pattern that is not at the start of the string
result = re.search(r'LOG', 'SOME LOGS')
print('pattern: LOG, string: SOME LOGS\n{}\n'.format(result))

# Match a pattern that is only at the start of the string
result = re.search(r'^LOG', 'LOGS')
print('pattern: LOG, string: LOGS\n{}\n'.format(result))

result = re.search(r'^LOG', 'SOME LOGS')
print('pattern: ^LOG, string: SOME LOGS\n{}\n'.format(result))

# Match a pattern only at the end of the string
result = re.search(r'LOG$', 'SOME LOG')
print('pattern: LOG$, string: SOME LOG\n{}\n'.format(result))

result = re.search(r'LOG$', 'SOME LOGS')
print('pattern: LOG$, string: SOME LOGS\n{}\n'.format(result))

# Match the word thing (not excluding things)
STRING = 'something in the things se shows me'
result = re.search(r'thing', STRING)

print('pattern: thing, string: {}\n{}'.format(STRING, result))
print(STRING[:result.start()], '<start>', 
      STRING[result.start():result.end()], '<end>',
      STRING[result.end():], '\n')

result = re.search(r'\bthing', STRING)
print('pattern: \\bthing, string: {}\n{}'.format(STRING, result))
print(STRING[:result.start()], '<start>',
      STRING[result.start():result.end()], '<end>',
      STRING[result.end():], '\n')

# Match a pattern that's only numbers and dashes
result = re.search(r'[0123456789-]+', 'the phone number is 1234-567-890')
print(r'pattern: [012346789-]+, string: the phone number is 1234-567-890'
      '\n{}'.format(result))
print('group:',
      re.search(r'[0123456789-]+', 'the phone number is 1234-567-890').group(),
      '\n')

# Match an email address naively
result = re.search(r'\S+@\S+', 'my email is email.123@test.com')
print(r'pattern: \S+@\S+, string: my email is email.123@test.com',
      '\n{}'.format(result))
