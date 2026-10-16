from follow import follow
import csv
import report
import tableformat

def convert_types(rows, types):
    for row in rows:
        try:
            yield [func(val) for func, val in zip(types, row)]

        except ValueError:
            continue

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = ([row[0], row[1], row[4]] for row in rows)
    rows = convert_types(rows, [str, float, float])
    rows = (dict(zip(['name', 'price', 'change'], row)) for row in rows)
    return rows

def ticker(portfile, logfile, fmt):
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['name', 'price', 'change'])
    for row in rows:
        rowdata = [row['name'], str(row['price']), str(row['change'])]
        formatter.row(rowdata)

if __name__ == '__main__':
    ticker('Data/portfolio.csv', 'Data/stocklog.csv', 'txt')