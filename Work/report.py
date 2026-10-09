import fileparse
import sys

def read_portfolio(filename):
    with open(filename) as f:
        portfolio = fileparse.parse_csv(f, types=[str, int, float])

    return portfolio

def read_prices(filename):
    with open(filename) as f:
        prices = fileparse.parse_csv(f, types=[str, float], has_headers=False)

    return dict(prices)

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

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)

if __name__ == '__main__':
    main(sys.argv)