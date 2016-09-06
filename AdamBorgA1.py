""" Name: Adam Borg
    date: 09/09/2016
    Program Details: Shopping list allows the user to open a csv file and then read and write to it depending on what
                     they need from the store. Each item in the list can also be assigned a priority of importance.
    GitHub Link: https://github.com/AdamBorg/AdamBorgA1.git"""


def main():

    import csv

    open_list = csv.reader(open("items.csv", 'r'))
    user_input = 'i'

    item_count = 0
    shopping_list = []
    count = -1

    for row in open_list:
        shopping_list.append(row)

        item_count += 1

    shopping_list = sorted(shopping_list, key = lambda shopping_list: shopping_list[2])

    print("Hi Welcome to Shopping List 1.0 - by Adam Borg \n{} items loaded from items.csv".format(item_count))

    while user_input != 'q':
        print("Menu: \nR - List Required items \nC - List completed items \nA - Add new item \nM - Mark an item as completed \nQ - Quit")
        user_input = str(input().lower())

        if user_input == 'r':
            for item_information in shopping_list:
                count += 1
                if item_information[3] == 'r':
                    print("{}. {:17} ${:5.2f} ({})".format(count, item_information[0], float(item_information[1]), item_information[2]))





main()
