""" Name: Adam Borg
    date: 09/09/2016
    Program Details: Shopping list allows the user to open a csv file and then read and write to it depending on what
                     they need from the store. Each item in the list can also be assigned a priority of importance.
    GitHub Link: https://github.com/AdamBorg/AdamBorgA1.git"""


def main():
    user_input = 'Initiate Variable'

    shopping_list = load_items()
    shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])

    print("Hi Welcome to Shopping List 1.0 - by Adam Borg \n{} items loaded from items.csv".format(len(shopping_list)))

    while user_input != 'q':
        print("Menu: \nR - List Required items \nC - List completed items \nA - Add new item \nM - Mark an item as "
              "completed \nQ - Quit")
        user_input = str(input().lower())

        if user_input not in 'rcamq':
            print("Invalid menu choice")

        if user_input == 'c' or user_input == 'r':
            print_lists(shopping_list, user_input)
            shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])

        elif user_input == 'm':
            shopping_list = complete_an_item(shopping_list, user_input)


        elif user_input == 'a':
            shopping_list = add_items(shopping_list)

    from csv import writer
    open_write = writer(open("items.csv", 'w', newline=''))

    for items in shopping_list:
        open_write.writerow(items)


def add_items(shopping_list):
    add_item = [0, 0, 0, 0]
    add_item[0] = str(input("Item name: "))
    add_item[1] = str(input("Price: $"))
    add_item[2] = str(input("Priority: "))
    add_item[3] = 'r'
    shopping_list.append(add_item)
    shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])
    print(shopping_list)
    return shopping_list


def complete_an_item(shopping_list, user_input):
    anymore_items = print_lists(shopping_list, user_input)
    if anymore_items != 0:
        shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[3], reverse=True)
        item_selected = int(input("Enter the number of an item to mark as completed?\n"))
        shopping_list[item_selected][3] = 'c'
        print("{} marked as completed".format(shopping_list[item_selected][0]))
        shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])
    return shopping_list


def load_items():
    from csv import reader
    open_read = reader(open("items.csv", 'r', ))
    shopping_list = []
    for row in open_read:
        shopping_list.append(row)

    return shopping_list


def print_lists(shopping_list, user_input):
    list_count = -1
    number_of_items = 0

    if user_input == 'm':
        user_input = 'r'

    if user_input == 'c':
        list_type = 'completed'
    else:
        list_type = 'required'

    for item_information in shopping_list:

        if item_information[3] == user_input:
            list_count += 1
            number_of_items += 1
            print("{}. {:17} ${:5.2f} ({})".format(list_count, item_information[0], float(item_information[1]),
                                                   item_information[2]))
    total_cost = 0
    for item_information in shopping_list:
        if item_information[3] == user_input:
            total_cost += float(item_information[1])

    if total_cost == 0:
        print("No {} items".format(list_type))
    else:
        print("Total expected price for {} items: $ {:.2f}".format(number_of_items, total_cost))

    return total_cost


main()
