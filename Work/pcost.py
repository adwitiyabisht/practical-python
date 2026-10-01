# pcost.py
#
# Exercise 1.27 and Exercise 1.28

def portfolio_cost(filename):
    total = 0.00

    with open(filename, 'rt') as data:
        header = next(data).split(',')

        for line in data:
            try:
                row = line.split(',')
                total += float(row[1]) * float(row[2])
            except ValueError:
                print(f"Couldn't parse: {line}")

    return total

cost = portfolio_cost('Data/missing.csv')

print(f"Total cost {cost:.2f}")