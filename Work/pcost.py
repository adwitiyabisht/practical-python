# pcost.py
#
# Exercise 1.27 and Exercise 1.28

import csv
import sys

def portfolio_cost(filename):
    total = 0.00

    with open(filename, 'rt') as data:
        rows = csv.reader(data)
        headers = next(rows)

        for rowno, row in enumerate(rows, start = 1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record['shares'])
                price = float(record['price'])
                total += nshares * price
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfoliodate.csv'

cost = portfolio_cost(filename)

print(f"Total cost {cost:.2f}")