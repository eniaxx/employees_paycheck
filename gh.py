# Boolean flag (does not accept input data), with default value
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-a1', action="store_true", default=False)

# Cast input to integer, with a default value
parser.add_argument('-a2', type=int, default=0)

# Provide long form name as well (maps to 'argument3' not 'a3')
parser.add_argument('-a3', '--argument3', type=str)

# Make argument mandatory
parser.add_argument('-a4', required=True)

# Retur the input via different parameter name
parser.add_argument('-a5', '--argument5', dest='my_argument')

args = parser.parse_args()
print(args.a1)
print(args.a2)
print(args.argument3)
print(args.a4)
print(args.my_argument)