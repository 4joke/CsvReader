#!/usr/bin/python
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--file", help="file location", type=str)
parser.add_argument("--comment", help="comment which we are looking for", nargs='+')
parser.add_argument("--category", help="category which we are looking for", nargs='+')
args = parser.parse_args()


def calculate(file, comment):
    summa = 0
    string = ''
    for word in comment:
        string+=word + " "
    with open(file, newline='', encoding='utf-8') as csvfile:
        scvreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        if args.comment:
            position = -1
        elif args.category:
            position = 2
        for row in scvreader:
            if row[position] == string.strip():
                summa += float(row[3].replace("\"", '').replace(",", ''))
    print(summa)


if args.file and args.comment:
    calculate(args.file, args.comment)
if args.file and args.category:
    calculate(args.file, args.category)
