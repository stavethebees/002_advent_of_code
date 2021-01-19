_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [i for i in file.read().splitlines()]


def get_trees(input, right, down):
    _width = len(input[0])
    _height = len(input)
    _trees = 0
    _x = _y = 0

    while(_y < _height):
        _trees += input[_y][_x] == "#"
        _x += right
        _x %= _width
        _y += down

    return _trees

print(f"PART 1: {get_trees(_data, 3, 1)}")

_pattern = [(1,1), (3,1), (5,1), (7,1), (1,2)]
_sum = 1
for _x, _y in _pattern:
    _sum *= get_trees(_data, _x, _y)

print(f"PART 2: {_sum}")