# pcost.py
import csv
import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    total = sum([s['shares'] * s['price'] for s in portfolio])
    return total

def main(argv):
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        filename = 'Data/portfolio.csv'

    cost = portfolio_cost(filename)

    print(f"Total cost {cost:.2f}")

if __name__ == '__main__':
    main(sys.argv)