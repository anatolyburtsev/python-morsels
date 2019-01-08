import csv
import argparse

parser = argparse.ArgumentParser(description='arg parser')
parser.add_argument("--in-delimiter", dest='delimiter', default=None)
parser.add_argument("--in-quote", dest='quote', default=None)
parser.add_argument("files", nargs=2)

args = parser.parse_args()
input_file, output_file = args.files
delimiter = args.delimiter
quote = args.quote

with open(input_file, 'r') as f:
    text = f.readlines()
    if delimiter is None and quote is None:
        # smart detect delimiter and quote
        dialect = csv.Sniffer().sniff("".join(text))
        csv.register_dialect("custom_dialect", dialect)
    else:
        # force set delimiter and quote
        if delimiter is None:
            delimiter = ","
        if quote is None:
            quote = '"'
        csv.register_dialect("custom_dialect", delimiter=delimiter,
                             quotechar=quote)

    data = list(csv.reader(text, dialect="custom_dialect"))

with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerows(data)
