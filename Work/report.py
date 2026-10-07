import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as data:
        rows = csv.reader(data)
        next(rows)

        for row in rows:
            try:
                holding = {}
                holding['name'] = row[0]
                holding['shares'] = int(row[1])
                holding['price'] = float(row[2])
                portfolio.append(holding)
            except ValueError:
                pass

    return portfolio

def read_prices(filename):
    prices = {}

    with open(filename, 'rt') as data:
        rows = csv.reader(data)

        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except (ValueError, IndexError):
                pass

    return prices

def make_report(stocks, prices):
    # name - shares - price - change
    report = []
    for s in stocks:
        change = prices[s['name']] - s['price']
        tup = (s['name'], s['shares'], prices[s['name']], change)
        report.append(tup)

    return report

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')

print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- -----------')

for name, shares, price, change in report:
    price_str = f"${price:.2f}"
    print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')