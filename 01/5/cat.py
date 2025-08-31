import sys

target = sys.argv[1]

with open(target, 'r') as f:
    print(f.read())