# The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if
# that character appears only once in the original string, or ")" if that character appears more than once in the
# original string. Ignore capitalization when determining if a character is a duplicate. Examples
#
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("
#
# Notes
#
# Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
# the "XXX" is the expected result, not the input! https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# def duplicate_encode_v1(string):
#     letter_counter = {}
#     result_string = ""
#     string = string.lower()
#     for letter in string:
#         letter_counter[letter] = letter_counter.get(letter, 0) + 1
#     for letter in string:
#         if letter_counter[letter] == 1:
#             result_string += '('
#         else:
#             result_string += ')'
#     return result_string


def duplicate_encode_(string):
    string = string.lower()
    return ''.join(['(' if string.count(letter) == 1 else ')' for letter in string])


# print(duplicate_encode_v2("din"))
