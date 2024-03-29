# Create a function with two arguments that will return an array of the first n multiples of x.
#
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
#
# Return the results as an array or list ( depending on language ).


def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

    # i = 1
    # results = []
    # while i < n:
    #     if i % x == 0:
    #         results.append(i)
    #     i = i + 1
    # return results
    #
