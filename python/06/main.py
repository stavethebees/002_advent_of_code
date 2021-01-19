_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [_.split() for _ in file.read().split("\n\n")]


def pt1(data):
    _datacompact = ["".join(_) for _ in data]
    _sum = 0
    for _entry in _datacompact:
        _set = set()
        for _ in _entry:
            _set.add(_)
        _sum += len(_set)
    return _sum


def pt2(data):
    _valid = 0
    for _entry in data:
        _numentries = len(_entry)
        _dict = dict() 
        for _person in _entry:
            for _char in _person:
                _dict.setdefault(_char, 0)
                _dict[_char] += 1
                if _dict[_char] == _numentries:
                    _valid += 1
    return _valid


print(f"PART 1: {pt1(_data)}")
print(f"PART 2: {pt2(_data)}")