"""
This module illustrates how to prepare a task for automation using argparse
and PyYAML. It reads the arguments from another file, in this case a YAML 
file. The code also saves the output into another file.
"""
import sys
import yaml
import argparse

def main(number, other_number, output):
    result = number * other_number
    print(f'The result is {result}', file=output)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n1', type=int, help='a number', default=1)
    parser.add_argument('-n2', type=int, help='another number', default=1)
    parser.add_argument('-c', dest='config', type=argparse.FileType('r'),
                        help='config file in YAML format', default=None)
    parser.add_argument('-o', dest='output', type=argparse.FileType('w'),
                        help='output file', default=sys.stdout)

    args = parser.parse_args()

    if args.config:
        config = yaml.load(args.config, Loader=yaml.FullLoader)

        # Transforming values into integers
        args.n1 = config['ARGUMENTS']['n1']
        args.n2 = config['ARGUMENTS']['n2']

    main(args.n1, args.n2, args.output)
