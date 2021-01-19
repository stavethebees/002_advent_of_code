import re

_handle = "test.txt"
_handle = "input.txt"


with open(_handle, "r") as _file:
    _input = _file.read().splitlines()


def pt1(input):
    return sum((int(_lo) <= _pass.count(_char) <= int(_hi)) for _lo, _hi, _char, _pass in input)


def pt2(input):
    return sum(bool(_pass[int(_lo) - 1] == _char) ^ bool(_pass[int(_hi) - 1] == _char) for _lo, _hi, _char, _pass in input)


_data = []
for _line in _input:
    _data.append(re.split(r"[-\s:]+", _line))


print(f"PART 1: {pt1(_data)}")
print(f"PART 2: {pt2(_data)}")