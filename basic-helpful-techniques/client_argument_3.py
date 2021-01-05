"""
This module illustrates code that accepts a single integer, a character, and an
uppercase flag as positional arguments and print this character 'n' amount of
times. If the uppercase flag is set to true, it prints uppercased.
"""
import argparse

def main(character, number):
    print (character * number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('-c', type=str,
            help='Character to print (defaults to #)', default='#')
    parser.add_argument('-U', action='store_true', default=False,
            dest='uppercase', help='Uppercase the character (defaults to False)')
    args = parser.parse_args()

    if args.uppercase:
        args.c = args.c.upper()
    main(args.c, args.number)
