import random

list_of_char = []


def init_list_character():
    """init the list with key and value to zero"""

    i = 0
    while i <= 255:
        list_of_char.append({"count": 0, "first": 0, "last": 0, "letter_before": [], "letter_after": []})
        i += 1


def count_character(name):
    """
    Count for each letter the first and last place, number of time when appears and letter before and after this
    name : string
    """

    name = name.lower()
    list_of_char[ord(name[0])]["first"] += 1
    list_of_char[ord(name[-1])]["last"] += 1

    i = 0
    while i < len(name):

        if ord(name[i]) > 33:
            list_of_char[ord(name[i])]["count"] += 1

            if i > 1:
                if ord(name[i - 1]) > 33:
                    list_of_char[ord(name[i])]["letter_before"].append(ord(name[i - 2]))

            if i < len(name) - 1:
                if ord(name[i + 1]) > 33:
                    list_of_char[ord(name[i])]["letter_after"].append(ord(name[i + 1]))
        i += 1


def print_list():
    """Print list of characters"""

    i = 0
    while i < len(list_of_char):
        if list_of_char[i]["count"] > 0:
            print(str(i) + " : " + chr(i) + " " + str(list_of_char[i]))

        i += 1


def count_list():
    init_list_character()

    list_of_name = open("name_list.txt")

    for n in list_of_name:
        count_character(n)


def choose_first_letter():
    list_letter_depends_percentage = []

    i = 0
    while i < len(list_of_char):
        j = 0
        while j < list_of_char[i]['first']:
            list_letter_depends_percentage.append(i)
            j += 1

        i += 1

    return random.choice(list_letter_depends_percentage)


def choose_letter(letter_index):
    try:
        return random.choice(list_of_char[letter_index]['letter_after'])
    except IndexError:
        return 0


def choose_last_letter(letter_index):
    list_letter_depends_percentage = []

    for letter in list_of_char[letter_index]['letter_after']:
        j = 0
        while j < list_of_char[letter]['last']:
            list_letter_depends_percentage.append(letter)
            j += 1
    if len(list_letter_depends_percentage) > 0:
        return random.choice(list_letter_depends_percentage)
    else:
        return 0


def generate_name(size):
    name = chr(choose_first_letter())

    for word_length in range(size):
        cont = True
        while cont:
            letter = choose_letter(ord(name[-1]))
            name = name + chr(letter)
            cont = False

    name = name + chr(choose_last_letter(ord(name[-1])))
    return name.capitalize()


if __name__ == '__main__':
    handle_size = ""
    number_of_name = ""

    count_list()
    choose_first_letter()

    while not handle_size.isdigit():
        handle_size = input("Enter handle's size : ")

    while not number_of_name.isdigit():
        number_of_name = input("Enter number of name : ")

    for i in range(int(number_of_name)):
        print(generate_name(int(handle_size)))
