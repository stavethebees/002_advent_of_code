_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [_ for _ in file.read().splitlines()]


_y = 1  # instead of making this 0.8660 for regular grid, made it 1, for ease
_directions = {
    "e": (1, 0),
    "w": (-1, 0),
    "ne": (0.5, _y),
    "nw": (-0.5, _y),
    "se": (0.5, -_y),
    "sw": (-0.5, -_y),
}

def expand_tiles(tiles, directions):
    _active_tiles = tiles.keys()
    _new_tiles = set()
    for _tile, _val in tiles.items():
        _x, _y = _tile
        for _, _direction in directions.items():
            _newpos = _x + _direction[0], _y + _direction[1]
            if _newpos not in _active_tiles:
                _new_tiles.add(_newpos)
    for _new_tile in _new_tiles:
        tiles[_new_tile] = 1
    return tiles


def solve_tick(tiles, directions):

    def get_black_neighbor_tiles(tile):
        _black_tiles = 0
        _active_tiles = tiles.keys()
        _x, _y = tile
        for _, _direction in directions.items():
            _newpos = _x + _direction[0], _y + _direction[1]
            if _newpos in _active_tiles:
                _black_tiles -= min(0, tiles[_newpos])
        return abs(_black_tiles)

    _flip_dict = dict()
    tiles = expand_tiles(tiles, directions)
    for _pos, _flip in tiles.items():
        _neighbors = get_black_neighbor_tiles(_pos)
        if _flip == -1:  # black
            if _neighbors == 0 or _neighbors > 2:
                _flip_dict[_pos] = 1
        else:
            if _neighbors == 2:
                _flip_dict[_pos] = -1
    tiles.update(_flip_dict)
    return tiles


def build_tile_map(data, directions):
    # 1 is white tile, -1 is black
    _tiles = {
        (0, 0): 1
    }

    for _instruction in data:
        _pos = [0, 0]
        _idx = 0
        _current_tile = tuple()
        while _idx < len(_instruction):
            _dir = _instruction[_idx]
            if _dir in ["e", "w"]:
                _idx += 1
            else:
                _dir = _instruction[_idx: _idx + 2]
                _idx += 2
            _x, _y = directions[_dir]
            _pos[0] += _x
            _pos[1] += _y
            _current_tile = (_pos[0], _pos[1])
        if _current_tile not in _tiles:
            _tiles[_current_tile] = -1
        else:
            _tiles[_current_tile] *= -1

    return _tiles


_tiles = build_tile_map(_data, _directions)
print(f"PART 1: {abs(sum([_v for _k, _v in _tiles.items() if _v == -1]))}")

for _i in range(100):
    _tiles = solve_tick(_tiles, _directions)

print(f"PART 2: {abs(sum([_v for _k, _v in _tiles.items() if _v == -1]))}")
