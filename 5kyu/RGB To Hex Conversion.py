# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
# representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
# must be rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.
# Examples (input --> output):
#
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"


def clamp_value(value, min_value=0, max_value=255):
    return max(min_value, min(value, max_value))


def rgb(r, g, b):
    r = '%02x' % clamp_value(r)
    g = '%02x' % clamp_value(g)
    b = '%02x' % clamp_value(b)
    hex_value = f'{r}{g}{b}'
    return hex_value.upper()

