

_monster = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""



def rotate_tile(tile, turn="left"):
    return tile


def rotate_to_rest_xform(tile, direction):
    if direction == 1: return tile
    _turns = direction
    for i in range(1, _turns):
        tile = rotate_tile_left(tile)
        # pprint(tile)
    return tile

    def get_matching_edges_for_all(edges_dict):
    # _matching_edgecount_dict = dict()
    # for _tile in edges_dict.keys():
    #     for _edge in edges_dict[_tile]:
    #         for _othertile, _otheredges in edges_dict.items():
    #             if _othertile == _tile:
    #                 continue
    #             if _edge in _otheredges:
    #                 _matching_edgecount_dict[_tile] = _matching_edgecount_dict.get(_tile, 0)
    #                 _matching_edgecount_dict[_tile] += 1
    #                 print("edge matched, this tile, edge, othertile:", _tile, _edge, _othertile)
    # return _matching_edgecount_dict


# pprint(_matching_edge_tile_dict)
# print(get_matching_edges(1951, 2311, _edges_dict))
# for _tile, _adjacent_tiles in _matching_edge_tile_dict.items():
    # for _adjacent_tile in _adjacent_tiles:
        # print("this tile", _tile, "adjacent tile", _adjacent_tile, "=", get_matching_edges(_tile, _adjacent_tile, _edges_dict))
        

def check_other_tiles(tile_num, edges_dict):
    # 1 - top, 2 - right, 3 - bottom, 4 - left
    _matching_edge_dict = {_k: [] for _k in edges_dict.keys()}
    _nonreversed_edges_dict = edges_dict[tile_num][:4]
    for _idx, _edge in enumerate(_nonreversed_edges_dict):
        for _othertile, _otheredges in edges_dict.items():
            if _othertile == tile_num:
                continue
            if _edge in _otheredges:
                _otheridx = _otheredges.index(_edge) + 1
                if _otheridx > 4:
                    _otheridx %= 4 * -1 
                # print("other tile_num matched:", _othertile, "this idx:", (_idx + 1), "other edge idx:", _otheridx)
                _matching_edge_dict[tile_num].append((_othertile, _otheridx))
    return _matching_edge_dict

    # 1277: {1993, 2141, 3301, 3767},



def is_valid_match_for_tile(tile, othertile, this_edge_num, edges_dict):
    return False
    for _adjacent_tile in _adjacent_tiles:
        _num_adjacent = len(get_adjacent_tiles(_adjacent_tile, _edges_dict))
        if _adjacent_tile in _added_to_image:
            # _num_adjacent -= 1
            continue
        if _num_adjacent < _min_adjacent_tiles:
            _min_adjacent_tiles = _num_adjacent
            _next_tile = _adjacent_tile


            # print(1201, 1549, get_matching_edges(1201, 1549, _edges_dict))
# print(1201, 2377, get_matching_edges(1201, 2377, _edges_dict))
# print(2161, 2689, get_matching_edges(2161, 2689, _edges_dict))
# print(2161, 2657, get_matching_edges(2161, 2657, _edges_dict))
# print(2927, 3617, get_matching_edges(2927, 3617, _edges_dict))
# print(2927, 2239, get_matching_edges(2927, 2239, _edges_dict))
# print(2753, 2621, get_matching_edges(2753, 2621, _edges_dict))
# print(2753, 2203, get_matching_edges(2753, 2203, _edges_dict))
            
    _flattened_image = '\n'.join(_final_image)
    _matches = re.findall(_regex, _flattened_image)
    _num_monsters = len(_matches)
    _hashes_in_monster_lines = sum(map(lambda x: x.count("#"), _matches))
    # print(_num_monsters, _monster_hashes, _hashes_in_monster_lines, _total_hashes)
    _water_roughness = (_total_hashes - _hashes_in_monster_lines) + (_hashes_in_monster_lines - _monster_hashes * _num_monsters)
    # print(_water_roughness)