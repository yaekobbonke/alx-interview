#!/usr/bin/python3
""" UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): The data set represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.

    Notes:
        - A character in UTF-8 can be 1 to 4 bytes long.
        - The data set can contain multiple characters.
        - Each integer represents 1 byte of data, therefore you only
        need to handle the 8 least significant bits of each integer.
    """

    num_bytes = 0

    for byte in data:
        if num_bytes > 0 and (byte & 0b11000000) == 0b10000000:
            num_bytes -= 1
        elif num_bytes == 0:
            mask = 0b10000000
            while (byte & mask) == mask:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0 or num_bytes > 4:
                return False

            if (byte & 0b11000000) == 0b10000000:
                return False
        else:
            return False

    return num_bytes == 0
