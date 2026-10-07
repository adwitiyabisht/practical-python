# pcost.py
#
# Exercise 1.27 and Exercise 1.28

import sys

def portfolio_cost(filename):
    total = 0.00


    with open(filename, 'rt') as data:
        header = next(data).split(',')

        for line in data:
            row = line.strip().split(',')
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Couldn't parse: {line.strip()}")

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)

print(f"Total cost {cost:.2f}")