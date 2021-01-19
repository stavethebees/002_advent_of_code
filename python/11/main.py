_handle = "test.txt"
_handle = "input.txt"

_data = []
with open(_handle, 'r') as _file:
    for _ in _file.read().splitlines():
        _data.append(list(_))


def num_occupied_adjacent(data, x, y):
    _occupied = 0
    _width = len(data[0])
    _height = len(data)
    _minx = max(0, x - 1)
    _maxx = min(_width - 1, x + 1)
    _miny = max(0, y - 1)
    _maxy = min(_height - 1, y + 1)

    for _y in range(_miny, _maxy + 1):
        for _x in range(_minx, _maxx + 1):
            if _x == x and _y == y: continue
            _occupied += data[_y][_x] == "#"

    return _occupied


def num_occupied_in_direction(data, x, y, direction):
    _length = len(data[0])
    _height = len(data)
    while (True):
        x += direction[0]
        y += direction[1]
        if (x not in range(0, _length) or y not in range(0, _height) or data[y][x] == "L"):
            return 0
        if data[y][x] == "#":
            return 1


def solve_single_tick_pt1(data):
    _data = [_ [:] for _ in data] # make a local copy
    _changes = 0
    for _y, _list in enumerate(_data):
        for _x, _item in enumerate(_list):
            if num_occupied_adjacent(_data, _x, _y) == 0 and _item == "L":
                data[_y][_x] = "#"
                _changes += 1
            elif num_occupied_adjacent(_data, _x, _y) >= 4 and _item == "#":
                data[_y][_x] = "L"
                _changes += 1
    return data, _changes


def solve_singletick_pt2(data):
    _directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1,1)]
    _changes = 0
    _data = [_ [:] for _ in data] # local copy
    for _y, _list in enumerate(_data):
        for _x, _item in enumerate(_list):
            _occupied = 0

            for _dir in _directions:
                _occupied += num_occupied_in_direction(_data, _x, _y, _dir)

            if _occupied == 0 and _item == "L":
                data[_y][_x] = "#"
                _changes += 1
            elif _occupied >= 5 and _item == "#":
                data[_y][_x] = "L"
                _changes += 1

    return data, _changes


def run_seat_simulation(data, part=1, max_iterations = 300):
    _data = [_ [:] for _ in data]
    _count = 0
    if part == 1:
        while(_count < max_iterations):
            _changes = solve_single_tick_pt1(_data)
            if _changes[1] == 0:
                break
            _count += 1

    elif part == 2:
        while(_count < max_iterations):
            _changes = solve_singletick_pt2(_data)
            if _changes[1] == 0:
                break
            _count += 1

    return sum(_.count("#") for _ in _data)


print(f"PART 1: {run_seat_simulation(_data)}")
print(f"PART 2: {run_seat_simulation(_data, part=2)}")