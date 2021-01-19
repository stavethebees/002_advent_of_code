_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [int(_) for _ in file.read().splitlines()]


def get_first_weak_num(data, preamblelength):
    _pos = preamblelength
    _length = len(data)
    _current = 0

    while (_pos < _length):
        _current = data[_pos]
        _preamblelist = set(data[_pos - preamblelength:_pos])
        _count = 0
        for _i in _preamblelist:
            if (_current - _i) not in _preamblelist:
                _count += 1
                if _count == preamblelength:
                    return _current
        _pos += 1
    return 0


def get_contiguous_min_max(data, goal):
    _start = 0
    _end = _start + 1
    _sum = 0
    while(_end < len(data)):
        _list = data[_start: _end]
        _sum = sum(_list)
        if _sum == goal:
            return sum([min(_list), max(_list)])
        elif _sum < goal:
            _end += 1
        elif _sum > goal:
            _start += 1

    return 0


_resultpt1 = get_first_weak_num(_data, 25)
print(f"PART 1: {_resultpt1}")
print(f"PART 2: {get_contiguous_min_max(_data, _resultpt1)}")