def mix_strings(str1, str2):
    string = ""
    index_str1 = 0
    index_str2 = 0

    while index_str1 < len(str1) and index_str2 < len(str2):
        if str1[index_str1] <= str2[index_str2]:
            string += str1[index_str1]
            index_str1 += 1
        else:
            string += str2[index_str2]
            index_str2 += 1

    string += str1[index_str1:]
    string += str2[index_str2:]

    return string


def sort_string(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2
    first_part = string[:mid]
    second_part = string[mid:]

    return mix_strings(sort_string(first_part), sort_string(second_part))


def is_anagram(string1, string2):
    string1 = string1.lower()
    string2 = string2.lower()

    if not string1 or not string2:
        return (sort_string(string1), sort_string(string2), False)

    return (sort_string(string1), sort_string(string2), sort_string(
        string1) == sort_string(string2))
