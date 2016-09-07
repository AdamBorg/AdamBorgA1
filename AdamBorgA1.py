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

    for row in open_list:
        shopping_list.append(row)

        item_count += 1

    shopping_list = sorted(shopping_list, key = lambda shopping_list: shopping_list[2])
    print(shopping_list)
    print("Hi Welcome to Shopping List 1.0 - by Adam Borg \n{} items loaded from items.csv".format(item_count))

    while user_input != 'q':
        print("Menu: \nR - List Required items \nC - List completed items \nA - Add new item \nM - Mark an item as "
              "completed \nQ - Quit")
        user_input = str(input().lower())

        if user_input == 'c':
            complete_list(shopping_list)

        elif user_input == 'r':
            registered_list(shopping_list)

        elif user_input == 'm':
            registered_list(shopping_list)
            item_selected = int(input("Enter the number of an item to mark as completed?\n"))
            shopping_list[item_selected][3] = 'c'
            print("{} marked as completed".format(shopping_list[item_selected][0]))
            shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[3], reverse=True)

def registered_list(shopping_list):
    list_count = -1
    number_of_items = 0

    for item_information in shopping_list:

        if item_information[3] == 'r':
            list_count += 1
            number_of_items += 1
            print("{}. {:17} ${:5.2f} ({})".format(list_count, item_information[0], float(item_information[1]),
                                                   item_information[2]))
    total_cost = 0
    for item_information in shopping_list:
        if item_information[3] == 'r':
            total_cost += float(item_information[1])

    print("Total expected price for {} items: $ {:.2f}".format(number_of_items, total_cost))

def complete_list(shopping_list):
    list_count = -1
    number_of_items = 0

    for item_information in shopping_list:

        if item_information[3] == 'c':
            list_count += 1
            number_of_items += 1
            print("{}. {:17} ${:5.2f} ({})".format(list_count, item_information[0], float(item_information[1]),
                                                   item_information[2]))
    total_cost = 0
    for item_information in shopping_list:
        if item_information[3] == 'c':
            total_cost += float(item_information[1])

    if total_cost == 0:
        print("No completed items")
    else:
        print("Total expected price for {} items: $ {:.2f}".format(number_of_items, total_cost))

main()
