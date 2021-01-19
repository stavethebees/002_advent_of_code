_handle = "test.txt"
_handle = "input.txt"


with open(_handle, 'r') as _file:
    _data = []
    for _ in _file.read().splitlines():
        _data.append(list(_))


def populate_active(data, dimensions=3):
    _active_cubes = set()
    for _y, _list in enumerate(data):
        for _x, _item in enumerate(_list):
            if _item == "#":
                if dimensions == 3:
                    _active_cubes.add((_x, _y, 0))
                elif dimensions == 4:
                    _active_cubes.add((_x, _y, 0, 0))
    return _active_cubes


def get_neighbor_cells(active_cubes, dimensions=3):
    _neighbors = set()
    _look = [-1, 0, 1]
    if dimensions == 4:
        for _x, _y, _z, _w in active_cubes:
            for _dx in _look:
                for _dy in _look:
                    for _dz in _look:
                        for _dw in _look:
                            _neighbors.add(
                                (_x + _dx, _y + _dy, _z + _dz, _w + _dw))
    else:
        for _x, _y, _z in active_cubes:
            for _dx in _look:
                for _dy in _look:
                    for _dz in _look:
                        _neighbors.add((_x + _dx, _y + _dy, _z + _dz))
    return _neighbors


def check_active_num(active_cubes, pos, dimensions=3):
    _active = 0
    _look = [-1, 0, 1]
    if dimensions == 4:
        _x, _y, _z, _w = pos
        for _dx in _look:
            for _dy in _look:
                for _dz in _look:
                    for _dw in _look:
                        _thispos = (_x + _dx, _y + _dy, _z + _dz, _w + _dw)
                        if _thispos in active_cubes and _thispos != pos:
                            _active += 1
    else:
        _x, _y, _z = pos
        for _dx in _look:
            for _dy in _look:
                for _dz in _look:
                    _thispos = (_x + _dx, _y + _dy, _z + _dz)
                    if _thispos in active_cubes and _thispos != pos:
                        _active += 1
    return _active


def solve(data, cycles, dimensions=3):
    _active_cubes = populate_active(data, dimensions)
    _counter = 0
    while(_counter < cycles):
        _nextstate = set()
        _neighbors_cells = get_neighbor_cells(_active_cubes, dimensions)
        for _thiscell in _neighbors_cells:
            _num_active = check_active_num(_active_cubes, _thiscell, dimensions)
            if (_num_active in (2, 3) and _thiscell in _active_cubes) or (_num_active == 3 and _thiscell not in _active_cubes):
                _nextstate.add(_thiscell)
        _active_cubes = _nextstate
        _counter += 1
    return len(_active_cubes)


print(f"PART 1: {solve(_data, 6)}")
print(f"PART 2: {solve(_data, 6, 4)}")
