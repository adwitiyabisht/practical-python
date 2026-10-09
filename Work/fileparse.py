import csv

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records.
    '''
    if select and not has_headers:
        raise RuntimeError('select argument requires column headers')

    if isinstance(lines, str):
        raise TypeError("Please pass a file-like object or list, not a string filename.")
    # Pass the new delimiter parameter directly to csv.reader
    rows = csv.reader(lines, delimiter=delimiter)

    if has_headers:
        headers = next(rows)
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

    records = []
    for row in rows:
        if not row:
            continue

        if has_headers and indices:
            row = [row[index] for index in indices]

        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {rows.line_num}: Couldn't convert {row}")
                    print(f"Row {rows.line_num}: Reason {e}")
                    continue

        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row) # Using tuple for headerless records

        records.append(record)

    return records