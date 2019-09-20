import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file location", type=str)
parser.add_argument("--comment", help="comment which we are looking for", nargs='+', required=True)
args = parser.parse_args()


def calculate(file, comment):
    summa = 0
    string = ''
    for word in comment:
        string+=word + " "
    with open(file, newline='', encoding='utf-8') as csvfile:
        scvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in scvreader:
            if row[-1] == string.strip():
                summa += float(row[3].replace("\"", ''))
    print(summa)


if args.file and args.comment:
    calculate(args.file, args.comment)
