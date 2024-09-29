# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python
#
# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
# Examples
#
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"
#


# take string
# separate by spaces
# take words
# reverse words
# build a string out of results

def reverse_words(text):
    # Split the text by spaces to get individual words
    words = text.split(" ")

    # Reverse each word individually
    reversed_individual_words = [word[::-1] for word in words]

    # Join the reversed words back into a string with spaces
    return " ".join(reversed_individual_words)


# Test the function
print(reverse_words("zxc vbn asddasdasd"))  # Output: "cxz nbv dsdasddsa"
