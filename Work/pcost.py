# pcost.py
#
# Exercise 1.27 and Exercise 1.28

import gzip

total = 0.00

with gzip.open('Data/portfolio.csv.gz', 'rt') as data:
    header = next(data).split(',')

    for line in data:
        row = line.split(',')
        total += float(row[1]) * float(row[2])

print(f"Total cost {total:.2f}")