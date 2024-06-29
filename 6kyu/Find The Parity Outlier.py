# https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
# You are given an array (which will have a length of at least 3, but could be very large) containing integers. The
# array is either entirely comprised of odd integers or entirely comprised of even integers except for a single
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.
def find_outlier(integers):
    evens = [num for num in integers if (num & 1) == 0]
    odds = [num for num in integers if (num & 1) == 1]

    return evens[0] if len(evens) == 1 else odds[0]