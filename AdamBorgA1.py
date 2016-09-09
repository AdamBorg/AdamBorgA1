""" IT@JCU CP1404 Assignment 1
    Shopping List 1.0
    Name: Adam Borg
    date: 09/09/2016
    GitHub Link: https://github.com/AdamBorg/AdamBorgA1.git

Pseudocode:

function load_items()
    create a list to save items to
    open items.csv to read contents
    for every line in items.csv
        save line to the created list
    return the list to the main function

function complete an item(shopping_list, user_input)
    print the required items list
    save total costs of all items in required list to variable
    setup boolean variable make it equal to false
    if total costs is not equal to zero
       sort shopping list to move required items to top of list

        while run til loop is broken
            try:
                if boolean value is false
                    get user to enter what item they would like to complete
                    switch boolean value to true so that this input message w
                else:
                    get user to enter what item they would like to complete
                if item number chosen is above 0 and has not already been completed
                    break while loop
                else:
                    print error message
            except if user enters a character or string
                print error message
            except enters a number greater than the size of the list
                print error message
        mark the item as completed
        print message saying item as been completed
        resort list to be back in priority before return list to main
    return the list to main

"""

from csv import *


def main():
    """Shopping list allows the user to open a csv file and then read and write to it depending on what
    they need from the store. Each item in the list can also be assigned a priority of importance."""
    user_input = 'Initiate Variable'

    shopping_list = load_items()
    shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])

    print("Shopping List 1.0 - by Adam Borg \n{} items loaded from items.csv".format(len(shopping_list)))

    while user_input != 'q':
        print("Menu: \nR - List Required items \nC - List completed items \nA - Add new item \nM - Mark an item as "
              "completed \nQ - Quit")
        user_input = str(input().lower())

        # Error Check for Menu
        if user_input not in 'rcamq':
            print("Invalid menu choice")

        # Takes user inputs displays correct menu
        if user_input == 'c' or user_input == 'r':
            print_lists(shopping_list, user_input)
            shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])

        elif user_input == 'm':
            shopping_list = complete_an_item(shopping_list, user_input)

        elif user_input == 'a':
            shopping_list = add_items(shopping_list)

    # Write added and completed items back to list
    open_write = writer(open("items.csv", 'w', newline=''))

    for items in shopping_list:
        open_write.writerow(items)

    # Farewell message
    print("{} items saved to items.csv".format(len(shopping_list)))
    print("Have a nice day :)")


def add_items(shopping_list):
    """ Add items to the shopping the list"""
    # Get name of item and error check
    item_name = str(input("Item name: ").strip())
    while item_name == "":
        print("Input can not be blank")
        item_name = str(input("Item name: ").strip())

    # Get Price of item and error check
    while True:
        try:
            item_price = str(input("Price: $"))
            if float(item_price) >= 0:
                break
            else:
                print("Price must be >= $0")

        except ValueError:
            print("Invalid input; enter a valid number")

    # Get priority of item and error check
    while True:
        try:
            item_priority = str(input("Priority: "))
            if int(item_priority) <= 3 and int(item_priority) > 0:
                break
            else:
                print("Priority must be 1, 2 or 3")
        except ValueError:
            print("Invalid input; enter a valid number")

    #Set item status as required; print details of added item
    add_item = [item_name, item_price, item_priority, 'r']
    shopping_list.append(add_item)
    shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])
    print("{}, ${:.2f} (priority {}) added to shopping list".format(item_name, float(item_price), item_priority))
    return shopping_list


def complete_an_item(shopping_list, user_input):
    """ will mark the item in the shopping list as complete """
    # If total cost is equal to 0 there is no items of that status
    total_cost = print_lists(shopping_list, user_input)
    instruct_user = False

    # Get selected item from user; error check input; change item status
    if total_cost != 0:
        shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[3], reverse=True)

        while True:
            try:
                if instruct_user:
                    item_selected = int(input("Enter the number of an item to mark as completed?\n"))
                    instruct_user = True
                else:
                    item_selected = int(input())
                if item_selected >= 0 and shopping_list[item_selected][3] == 'r':
                    break
                else:
                    print("Invalid item number")
            except ValueError:
                print("Invalid input; enter a number")
            except IndexError:
                print("Invalid item number")
        shopping_list[item_selected][3] = 'c'
        print("{} marked as completed".format(shopping_list[item_selected][0]))
        shopping_list = sorted(shopping_list, key=lambda shopping_list: shopping_list[2])
    return shopping_list


def load_items():
    """ loads items from a csv file so that it can be used to see what is needed"""
    open_read = reader(open("items.csv", 'r', ))
    shopping_list = []
    for row in open_read:
        shopping_list.append(row)

    return shopping_list


def print_lists(shopping_list, user_input):
    """ prints list desired by user; calculates the total cost of that list """
    list_count = -1
    number_of_items = 0
    total_cost = 0

    # re-assign m to r as the registered list is required for completing an item
    if user_input == 'm':
        user_input = 'r'

    if user_input == 'c':
        list_type = 'Completed'
    else:
        list_type = 'Required'

    for item_information in shopping_list:
        if item_information[3] == user_input:
            total_cost += float(item_information[1])

    # print correct message to user; menu or no items
    if total_cost == 0:
        print("No {} items".format(list_type.lower()))
    else:
        print("{} items: ".format(list_type))
        for item_information in shopping_list:

            if item_information[3] == user_input:
                list_count += 1
                number_of_items += 1
                print("{}. {:17} ${:5.2f} ({})".format(list_count, item_information[0], float(item_information[1]),
                                                       item_information[2]))
        print("Total expected price for {} items: $ {:.2f}".format(number_of_items, total_cost))

    return total_cost


main()
