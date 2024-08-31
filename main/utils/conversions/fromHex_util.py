def hex_to_binary(number):
    # Convert the hex number to binary
    return bin(int(number, 16)).replace("0b", "")


def hex_to_int(number):
    # Convert the hex number to decimal
    return int(number, 16)
