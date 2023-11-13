import re


def check_if_is_number(text: str):
    try:
        int(text)
        return True
    except ValueError:
        return False

def get_all_numbers_in_a_sentence(text: str):
    return [int(i) for i in re.findall(r'[-+]?\d+', text)]

def get_all_numbers_in_a_sentence_with_comma(text: str):
    #remove comma in numbers
    text = text.replace(',', '')
    return [int(i) for i in re.findall(r'[-+]?\d+', text)]

def get_all_numbers(text: str):
    return get_all_numbers_in_a_sentence(text) + get_all_numbers_in_a_sentence_with_comma(text)
