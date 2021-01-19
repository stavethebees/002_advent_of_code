
def pt2(input):
    __valid = 0
    for _item in _data:
        _pass = _item[-1]
        _char = _item[-2]
        _lo = int(_item[0])
        _hi = int(_item[1])
        __valid += bool(_pass[_lo - 1] == _char) ^  bool(_pass[_hi - 1] == _char)
    return __valid


def pt1(input):
    __valid = 0
    for _item in _data:
        _pass = _item[-1]
        _char = _item[-2]
        _lo = int(_item[0])
        _hi = int(_item[1])
        if _pass.count(_char) in range(_lo, _hi + 1):
            __valid += 1
    return __valid
