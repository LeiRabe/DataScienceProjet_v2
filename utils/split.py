import os

def split(filehandler, delimiter='\t', row_limit=100000,
          output_name_template='output_%s.tsv', output_path='.', keep_headers=True):
    import csv
    csv.field_size_limit(10000000)
    reader = csv.reader(filehandler, delimiter=delimiter)
    current_piece = 1
    current_out_path = os.path.join(
        output_path,
        output_name_template % current_piece
    )
    current_out_writer = csv.writer(open(current_out_path, 'w', encoding="utf8", errors='ignore'), delimiter=delimiter)
    current_limit = row_limit
    if keep_headers:
        headers = next(reader)
        current_out_writer.writerow(headers)
    for i, row in enumerate(reader):
        if i + 1 > current_limit:
            current_piece += 1
            current_limit = row_limit * current_piece
            current_out_path = os.path.join(
                output_path,
                output_name_template % current_piece
            )
            current_out_writer = csv.writer(open(current_out_path, 'w', encoding="utf8", errors='ignore'), delimiter=delimiter)
            if keep_headers:
                current_out_writer.writerow(headers)
        current_out_writer.writerow(row)


if __name__ == '__main__':
    split(open('../Data_input/amazon_reviews_us_Books_v1_00.tsv', 'r', encoding="utf8", errors='ignore'))
