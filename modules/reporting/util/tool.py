import math
import re

BASE62 = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def split_timelist(keys, win_size):
    keys.sort()
    output = []
    timelist = []
    for key in keys:
        if timelist:
            if (int(key) - int(timelist[0])) <= win_size:
                timelist.append(key)
            else:
                output.append(timelist)
                timelist = list()
                timelist.append(key)
        else:
            timelist.append(key)
    if timelist:
        output.append(timelist)
    return output


def is_valid_reading(d):
    if not d:
        return False
    if math.isnan(d):
        return False
    if math.isinf(d):
        return False
    if d < 0:
        return False
    return True


def base62_encode(num, alphabet=BASE62):
    """Encode a positive number in Base X

    Arguments:
    - `num`: The number to encode
    - `alphabet`: The alphabet to use for encoding
    """
    num = int(num * 10)
    if num == 0:
        return "00"
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    result = ''.join(arr)
    if len(result) < 2:
        result = '0' + result
    return result


def base62_decode(string, alphabet=BASE62):
    """Decode a Base X encoded string into the number

    Arguments:
    - `string`: The encoded string
    - `alphabet`: The alphabet to use for encoding
    """
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base ** power)
        idx += 1

    return num / 10


def extract_num_from_str(str):
    return int(re.sub('[\D_]+', '', str))
