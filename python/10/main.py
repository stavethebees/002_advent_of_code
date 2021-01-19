# TODO: non recursive function, bottom up solution

_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [int(_) for _ in file.read().splitlines()]

def pt1(data):
    _length = len(data)
    _differences = [0, 0, 1] # preinclude 3 jolt device difference
    _pos = 0
    data.sort()

    while (_pos < _length - 1):
        _difference = data[_pos + 1] - data[_pos]
        _difference_idx = _difference - 1
        _differences[_difference_idx] += 1
        _pos += 1

    return _differences[0] * _differences[2]


def pt2(data):
    # watched a vid on dynamic programming/memoization for this
    # build prev candidates graph - each entry holds indices of valid prev candidates
    _seen = {}
    def num_paths_recursive(num):
        _val = 0
        if num in _seen:
            return _seen[num]
        if num == 0:
            return 1
        else:
            for _i in _prev_candidates[num]:
                _val += num_paths_recursive(_i)
        _seen[num] = _val
        return _val
    
    _length = len(data)
    _pos = _length - 1
    _prev_candidates = {i:[] for i in range(_length)}
    _tolerance = 3
    while (_pos > -1):
        # walk backwards, look behind 3 and add valid candidates to the dictionary
        for _i in range(_pos - 1, max(_pos - 4, -1), -1):
            if data[_pos] - data[_i] <= _tolerance:
                _prev_candidates[_pos].append(_i)
        _pos -= 1

    # do recursive function calls, cache previously calculated results
    return num_paths_recursive(_length - 1)


_data.append(0) # add in zero for wall socket
_data.sort()

print(f"PART 1: {pt1(_data)}")
print(f"PART 2: {pt2(_data)}")