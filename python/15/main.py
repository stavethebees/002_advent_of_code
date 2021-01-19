from collections import deque, defaultdict

_handle = "test.txt"
_handle = "input.txt"


with open(_handle, 'r') as file:
    _data = [int(_) for _ in file.read().split(",")]


def calculate(data, turns):
    # idea is to have a dictionary of seen numbers as keys and 
    # a corresponding queue which only keep last 2 positions where they were seen
    _turn = len(data)
    _lastnum = data[-1]
    _seen_dict = defaultdict(lambda: deque([-1, _turn]), 
                            {_num: deque([-1, _turn]) for _turn, _num in enumerate(data)})

    while (_turn < turns):
        if _lastnum in _seen_dict:
            if -1 in _seen_dict[_lastnum]:
                _lastnum = 0
            else:
                _lastnum = _seen_dict[_lastnum][1] - _seen_dict[_lastnum][0]

            _seen_dict[_lastnum].popleft()
            _seen_dict[_lastnum].append(_turn)

        else:
            _seen_dict[_lastnum] # add last num to seen dictionary
            _lastnum = 0

        _turn += 1
    return _lastnum
    


print(f"PART 1: {calculate(_data, 2020)}")
print(f"PART 2: {calculate(_data, 30000000)}") # takes 17 seconds to compute, need to optimize algo