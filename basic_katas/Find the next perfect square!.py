# You might know some pretty large perfect squares. But what about the NEXT one?
#
# Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter.
# Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.
#
# If the argument is itself not a perfect square then return either -1 or an empty value like None or null,
# depending on your language. You may assume the argument is non-negative.
#
# Examples:(Input --> Output)
#
# 121 --> 144
# 625 --> 676
# 114 --> -1 since 114 is not a perfect square
# https://www.codewars.com/kata/56269eb78ad2e4ced1000013/train/python
import math


def find_next_square(num):
    # NOT PERFECT SQUARES DROPPED HERE
    if round(math.sqrt(num)) ** 2 != num:
        return -1
    return int(((math.sqrt(num)) + 1) ** 2)


# print(find_next_square(121))
