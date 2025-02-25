import csv


def parse_csv(filename):
    output = []
    with open(filename, encoding="utf8") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for row in reader:
            output.append(row)
    return output
