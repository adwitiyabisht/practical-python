import csv

def read_portfolio(filename):
    portfolio = []

    with open(filename, 'rt') as data:
        rows = csv.reader(data)
        headers = next(rows)

        for row in rows:
            try:
                holding = dict(zip(headers, row))

                if 'shares' in holding:
                    holding['shares'] = int(holding['shares'])

                if 'price' in holding:
                    holding['price'] = float(holding['price'])

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

def print_report(report):
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print('---------- ---------- ---------- -----------')

    for name, shares, price, change in report:
        price_str = f"${price:.2f}"
        print(f'{name:>10s} {shares:>10d} {price_str:>10s} {change:>10.2f}')

def portfolio_report(portfolio_file, prices_file):
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)

portfolio_report('Data/portfolio.csv', 'Data/prices.csv')