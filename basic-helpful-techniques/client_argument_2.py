"""
This module illustrates code that accepts a single integer and a character 
to print as a positional arguments and print this character 'n' amount of times
"""
import argparse

def main(character, number):
    print (character* number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='A number')
    parser.add_argument('-c', type=str,
                        help='Character to print (defaults to #)', default='#')
    args = parser.parse_args()

    main(args.c, args.number)
