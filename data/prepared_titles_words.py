
import csv
import fileinput
from sys import stdout


def csv_readline(line):
    """Given a sting CSV line, return a list of strings."""
    for row in csv.reader([line]):
        return row


def main():
    csv_writer = csv.writer(stdout)

    for line in fileinput.input():
        cell = csv_readline(line)
        if cell[0] == 'A':
            words = cell[3].split(' ')
            for word in words:
                row = (word,1)
                csv_writer.writerow(row)


if __name__ == '__main__':
    main()
