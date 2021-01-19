_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [list(_) for _ in file.read().splitlines()]


def traverse(pos, instruction):
    _start, _end = pos
    _length = _end - _start
    _newpos = []
    if instruction in {"F", "L"}:
        _newpos = _start, _start + _length // 2
    else:
        _newpos = _start + _length // 2 + 1, _end
    return _newpos


def calc_seatID(instruction):
    _rows = 128
    _columns = 8
    _instructionA = instruction[:-3]
    _instructionB = instruction[-3:]
    _rowpos = 0, _rows - 1
    _columnpos = 0, _columns - 1
    while len(_instructionA) > 0:
        _rowpos = traverse(_rowpos, _instructionA.pop(0))
    while len(_instructionB) > 0:
        _columnpos = traverse(_columnpos, _instructionB.pop(0))

    return _rowpos[0] * _columns + _columnpos[0]


def find_highest_seatID(data):
    _highest_ID = -1
    for _instruction in data:
        _ID = calc_seatID(_instruction)
        _highest_ID = max(_highest_ID, _ID)
    return _highest_ID


def find_my_seat(data):
    _seatIDs = []
    for _instruction in data:
        _seatIDs.append(calc_seatID(_instruction))
    _seatIDs.sort()
    _candidate = _seatIDs[0]
    for _ID in _seatIDs:
        if _candidate != _ID:
            break
        _candidate += 1
    return _candidate


print(f"PART 1: {find_highest_seatID(_data)}")
print(f"PART 2: {find_my_seat(_data)}")