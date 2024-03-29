# Convert number to reversed array of digits
#
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.


def digitize(n):
    return [int(digit) for digit in reversed(str(n))]


    # result = []
    # n = str(n)
    # for _ in n:
    #     result.append(_)
    # print(result)
    # return reversed(result)
