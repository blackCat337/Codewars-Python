def remove_char(string):
    return string.replace("-", " ")


def parse_int(string):
    string_elements = remove_char(string)

    tens_dict = {
        "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
        "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90
    }

    numbers_dict = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
        "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
        "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
        "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
        "eighteen": 18, "nineteen": 19
    }

    hundreds_dict = {
        "hundred": 100, "thousand": 1000, "million": 1000000
    }

    string_elements = string_elements.split()
    final_number = 0
    temporary_number = 0

    for element in string_elements:
        if element in numbers_dict:
            temporary_number += numbers_dict[element]
        elif element in tens_dict:
            temporary_number += tens_dict[element]
        elif element == "hundred":
            temporary_number *= hundreds_dict[element]
        elif element in hundreds_dict:
            final_number += temporary_number
            temporary_number = 0
            final_number *= hundreds_dict[element]
        elif element in ["thousand", "million"]:
            final_number += temporary_number
            temporary_number = 0
            final_number *= hundreds_dict[element]
        elif element == "and":
            continue
        else:
            raise ValueError(f"Unrecognized word: {element}")

    final_number += temporary_number
    return final_number
