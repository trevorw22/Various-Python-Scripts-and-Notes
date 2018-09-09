# This is a command line calculator with various functions to help me learn how to parse cli arguments.

import argparse
import sys

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('--x', type=float, default=1.0, help='What is the first number?')
	parser.add_argument('--y', type=float, default=1.0, help='What is the second number?')
	parser.add_argument('--operation', type=str, default='add', help='What operation? (add, sub, mul, or div)')
	args = parser.parse_args()
	sys.stdout.write(str(calc(args))) #so that the output goes to the console itself

def calc(args): #we changed x, y, operation to just args b/c of the above code
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y

if __name__ == '__main__':
	main()

# operation = calc(7,3,'div')
# print(operation)
