""" Name: Adam Borg
    date: 09/09/2016
    Program Details: Shopping list allows the user to open a csv file and then read and write to it depending on what
                     they need from the store. Each item in the list can also be assigned a priority of importance.
    GitHub Link: https://github.com/AdamBorg/AdamBorgA1.git"""


def main():

    import csv

    open_list = csv.reader(open("items.csv", 'r'))

    item_count = 0
    shopping_list = []

    for row in open_list:
        shopping_list.append(row)

        item_count += 1

    print("Hi Welcome to Shopping List 1.0 - by Adam Borg \n{} items loaded from items.csv".format(item_count))

main()
