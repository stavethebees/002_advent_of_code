_handle = "test.txt"
_handle = "input.txt"

# this took me quite a lot of time! interested to know how i could have done this better

with open(_handle, 'r') as file:
    _raw_data = {int(_t.split(":")[0][5:]): _t.split(":")[1] for _t in file.read().split("\n\n")}


def get_edge_tuples(tile):
    _top = ''.join(tile[0])
    _btm = ''.join(tile[-1][::-1])
    _left = ''.join([i[0] for i in tile][::-1])
    _right = ''.join([i[-1] for i in tile])
    # 5 - 8 positions are reversed edges
    return (_top, _right, _btm, _left, _top[::-1], _right[::-1], _btm[::-1], _left[::-1])


def strip_edges(tile):
    tile.pop(-1)
    tile.pop(0)
    tile = [i[1:-1] for i in tile]
    return tile


def get_adjacent_tiles(tile_num, edges_dict):
    _adjacent_tiles = set()
    for _edge in edges_dict[tile_num]:
        for _othertile, _otheredges in edges_dict.items():
            if _othertile == tile_num:
                continue
            if _edge in _otheredges:
                _adjacent_tiles.add(_othertile)
    return _adjacent_tiles


def get_matching_tiles_for_all(edges_dict):
    _matching_edge_dict = {_k: {} for _k in edges_dict.keys()}
    for _tile_num in edges_dict.keys():
        _matching_edge_dict[_tile_num] = get_adjacent_tiles(_tile_num, edges_dict)
    return _matching_edge_dict


def flip_tile_x(tile):
    return [_l[::-1] for _l in tile]


def flip_tile_y(tile):
    return tile[::-1]


def rotate_tile_left(tile):
    _tile = []
    _length = len(tile)
    j = _length - 1
    for i in range(_length - 1, -1, -1):
        _sublist = []
        for j in range(_length):
            _sublist.append(tile[j][i])
        _tile.append(''.join(_sublist))
    return _tile


def rotate_tile_right(tile):
    _tile = []
    _length = len(tile)
    j = _length - 1
    for i in range(_length):
        _sublist = []
        for j in range(_length - 1, -1, -1):
            _sublist.append(tile[j][i])
        _tile.append(''.join(_sublist))
    return _tile


def get_matching_edges(tile_num, other_tile_num, edges_dict):
    _matching_edges = tuple()
    for _idx, _edge in enumerate(edges_dict[tile_num][:4]):
        _otheredges = edges_dict[other_tile_num]
        if _edge in _otheredges:
            _foundidx = _otheredges.index(_edge)
            # if it's found after idx 3, it's a reversed edge.
            if _foundidx > 3:
                _foundidx = (_foundidx % 4 + 1) * -1
            else:
                _foundidx += 1

            _thisidx = _idx + 1
            _matching_edges = (_thisidx, _foundidx)
    return _matching_edges


def orient_tile(tile, othertile, matching_edge, other_matching_edge):
    _sign = (1, -1)[other_matching_edge < 0]
    _turns = matching_edge - 1
    _localized_other_matching_edge = (((abs(other_matching_edge) - matching_edge) % 4) + 1) * _sign
    
    # rotate to local xform
    for i in range(_turns):
        tile = rotate_tile_left(tile)
        othertile = rotate_tile_left(othertile)

    # now we just need 1 set of instructions to rotate / flip all cases of the other tile
    if _localized_other_matching_edge == 1: othertile = flip_tile_y(othertile)
    elif _localized_other_matching_edge == 2: 
        othertile = flip_tile_y(othertile) 
        othertile = rotate_tile_right(othertile)
    elif _localized_other_matching_edge == 3:
        othertile = flip_tile_x(othertile)
    elif _localized_other_matching_edge == 4:
        othertile = flip_tile_y(othertile)
        othertile = rotate_tile_left(othertile)
    elif _localized_other_matching_edge == -1:
        othertile = flip_tile_y(othertile)
        othertile = flip_tile_x(othertile)
    elif _localized_other_matching_edge == -2:
        othertile = rotate_tile_right(othertile)
    elif _localized_other_matching_edge == -4:
        othertile = rotate_tile_left(othertile)

    # rotate back to original frame
    for i in range(_turns):
        othertile = rotate_tile_right(othertile)

    return othertile


_edges_dict = {_k: get_edge_tuples(_list.split()) for _k, _list in _raw_data.items()}
_processed_full_tiles = {_k: _list.strip().splitlines() for _k, _list in _raw_data.items()}

# -----------------  PART 1 
_matching_edge_tile_dict = get_matching_tiles_for_all(_edges_dict)
_result = 1
for _tile, _items in _matching_edge_tile_dict.items():
    if len(_items) == 2:
        _result *= _tile
print(f"PART 1: {_result}")


# -----------------  PART 2
_length = int(len(_edges_dict) ** 0.5)
_sorted_image_tile_ids = [[None] * _length for i in range(_length)]
_sorted_image_tiles = [[None] * _length for i in range(_length)]

_corner_tile_num = -1
# find a corner tile and flip it so that side 2 and 3 are pointing right and down respectively. 
# then update edges dict, and processed images
for _tile_num, _adjacent_tiles in _matching_edge_tile_dict.items():
    if len(_adjacent_tiles) == 2:
        _corner_tile_num = _tile_num
        _connected_sides = set()
        for _adjacent_tile in _adjacent_tiles:
            _connected_sides.add(get_matching_edges(_corner_tile_num, _adjacent_tile, _edges_dict)[0])

        _leftturns = 0
        if _connected_sides.issubset({3,4}):
            _leftturns = 1
        elif _connected_sides.issubset({4,1}):
            _leftturns = 2
        elif _connected_sides.issubset({1,2}):
            _leftturns = 3
        _this_tile = _processed_full_tiles[_corner_tile_num]
        for i in range(_leftturns):
            _this_tile = rotate_tile_left(_this_tile)
        _processed_full_tiles[_corner_tile_num] = _this_tile
        _edges_dict[_corner_tile_num] = get_edge_tuples(_this_tile)

        break

# traverse through list like a snake circling in 
_directions_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]
_direction_side_map = {0: 2, 1: 3, 2: 4, 3: 1}
_x, _y = 0, 0       # starting pos
_direction = 0
_sorted_image_tile_ids[_x][_y] = _corner_tile_num
_seen_positions = set()

for _i in range(_length * _length - 1):
    _this_tile = _sorted_image_tile_ids[_x][_y]

    _seen_positions.add((_x, _y))
    _dx, _dy = _directions_list[_direction][0], _directions_list[_direction][1]
    _newx, _newy = _x + _dx, _y + _dy
    if 0 <= _newx < _length and 0 <= _newy < _length and (_newx,_newy) not in _seen_positions:
        _x, _y = _newx, _newy
    else:
        _direction = (_direction + 1) % 4
        _x, _y = _x + _directions_list[_direction][0], _y + _directions_list[_direction][1]

    # get the next tile which matches
    _adjacent_tiles = get_adjacent_tiles(_this_tile, _edges_dict)
    _next_tile = -1
    _matching_side = _direction_side_map[_direction]
    for _adjacent_tile in _adjacent_tiles:
        _thisedge, _otheredge = get_matching_edges(_this_tile, _adjacent_tile, _edges_dict)
        if _thisedge == _matching_side:
            _next_tile = _adjacent_tile
            break

    # orient tile update tile and edges dict
    _oriented_next_tile = orient_tile(_processed_full_tiles[_this_tile], _processed_full_tiles[_next_tile], _matching_side, _otheredge)
    _processed_full_tiles[_next_tile] = _oriented_next_tile
    _edges_dict[_next_tile] = get_edge_tuples(_oriented_next_tile)

    # finally, add next tile to the correct position
    _sorted_image_tile_ids[_x][_y] = _next_tile


# remove borders
for _tile_num, _tile in _processed_full_tiles.items():
    _processed_full_tiles[_tile_num] = strip_edges(_tile)

# put tiles together
for _i, _sublist in enumerate(_sorted_image_tile_ids):
    for _j, _num in enumerate(_sublist):
        _sorted_image_tiles[_i][_j] = _processed_full_tiles[_num]

# stitch image together 
_stripped_tile_length = len(_sorted_image_tiles[0][0][0])
_final_image = []
for i in range(_length):
    for k in range(_stripped_tile_length):
        _line = []
        for j in range(_length):
            _line.append(_sorted_image_tiles[i][j][k])
        _final_image.append(''.join(_line))


_monster_pattern =['                  # ', '#    ##    ##    ###', ' #  #  #  #  #  #   ']
_monster_set = set()
for _i, _sublist in enumerate(_monster_pattern):
    for _j, _char in enumerate(_sublist):
        if _char == "#":
            _monster_set.add((_i, _j))

_length = len(_final_image[0])
_monsters = 0
for _thisx, _sublist in enumerate(_final_image):
    for _thisy, _char in enumerate(_sublist):
        _is_monster = False
        for _x, _y in _monster_set:
            _newx, _newy = _thisx + _x, _thisy + _y
            if max(_newx, _newy) > _length - 1:
                _is_monster = False
                break
            if _final_image[_newx][_newy] != "#":
                _is_monster = False
                break
            _is_monster = True
        _monsters += _is_monster
        

_roughness_list = []
_total_hashes =  sum(map(lambda x: x.count("#"), _final_image))

for i in range(8):
    _monsters = 0
    for _thisx, _sublist in enumerate(_final_image):
        for _thisy, _char in enumerate(_sublist):
            _is_monster = False
            for _x, _y in _monster_set:
                _newx, _newy = _thisx + _x, _thisy + _y
                if max(_newx, _newy) > _length - 1:
                    _is_monster = False
                    break
                if _final_image[_newx][_newy] != "#":
                    _is_monster = False
                    break
                _is_monster = True
            _monsters += _is_monster
    _roughness = _total_hashes - _monsters * len(_monster_set)
    _roughness_list.append(_roughness)
    if i == 4:
        _final_image = flip_tile_x(_final_image)
    _final_image = rotate_tile_left(_final_image)

print(f"PART 2: {min(_roughness_list)}")