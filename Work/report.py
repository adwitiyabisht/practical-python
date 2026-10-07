# report.py
#
# Exercise 2.4

import csv

'''
def portfolio_cost(filename):
    total = 0.00

    with open(filename, 'rt') as data:
        rows = csv.reader(data)
        next(rows)

        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print(f"Couldn't parse: {row}")

    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/missing.csv'

cost = portfolio_cost(filename)

print(f"Total cost {cost:.2f}")
'''

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as data:
        rows = csv.reader(data)
        next(rows)

        for row in rows:
            try:
                holding = (row[0], int(row[1]), float(row[2]))
                portfolio.append(holding)
            except ValueError:
                pass

    return portfolio

portfolio = read_portfolio("Data/missing.csv")

print(portfolio)