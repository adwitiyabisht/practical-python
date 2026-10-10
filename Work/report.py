import fileparse
import stock
import sys
import tableformat

def read_portfolio(filename):
    with open(filename) as f:
        portdicts = fileparse.parse_csv(f, types=[str, int, float])
        portfolio = [stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts]

    return portfolio

def read_prices(filename):
    with open(filename) as f:
        prices = fileparse.parse_csv(f, types=[str, float], has_headers=False)

    return dict(prices)

def make_report(stocks, prices):
    # name - shares - price - change
    report = []
    for s in stocks:
        change = prices[s.name] - s.price
        tup = (s.name, s.shares, prices[s.name], change)
        report.append(tup)

    return report

def print_report(report, formatter):
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in report:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_file, prices_file, fmt='txt'):
    # Read data files

    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    # Create the report data
    report = make_report(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    
    print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    format = argv[3]
    portfolio_report(portfile, pricefile, format)

if __name__ == '__main__':
    main(sys.argv)