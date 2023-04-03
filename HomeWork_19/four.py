import argparse

parser = argparse.ArgumentParser(add_help=False, description='myparser')

parser.add_argument('--name', '-n', type=str)
parser.add_argument('--help', '-h', action='store_true')

args = parser.parse_args()

if args.help:
    print('Some text')

if args.name is not None:
    if args.name == 'Oleksandr':
        print('Another text')
    else:
        print(f'Welcome, {args.name}!')





