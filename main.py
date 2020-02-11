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

            if i > 0:
                list_of_char[ord(name[i])]["letter_before"].append(ord(name[i - 1]))

            if i < len(name) - 1:
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

    print_list()


if __name__ == '__main__':
    count_list()
