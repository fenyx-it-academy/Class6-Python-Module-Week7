import csv
import os.path


def print_names():
    with open('users.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print("{} {}".format(row['first_name'], row['last_name']))


def add_name():
    file_exists = os.path.isfile('users.csv')
    with open('users.csv', 'a') as file:
        fieldnames = ['first_name', 'last_name']
        writer = csv.DictWriter(file, fieldnames)
        if not file_exists:
            writer.writeheader()
        first = input("First name please: ")
        last = input("Last name please: ")
        writer.writerow(dict(first_name=first, last_name=last))


add_name()
print_names()
