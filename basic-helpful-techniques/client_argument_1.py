"""
This module illustrates code that accepts a single integer as a positional
argument and print a hash symbol that amount of times
"""
import argparse

def main(number):
    print ('#' * number)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int, help='A number')
    args = parser.parse_args()

    main(args.number)
