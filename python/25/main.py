_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _publicA, _publicB = [int(_) for _ in file.read().splitlines()]
    

def find_loop_num(subject, key, divisor=20201227):
    _val = 1
    _loops = 0
    while (True):
        _val *= subject
        _val = _val % divisor
        if _val == key:
            break
        _loops += 1
    return _loops + 1


def transform_key(loopsize, subject, divisor=20201227):
    _val = 1
    for _ in range(loopsize):
        _val *= subject
        _val = _val % divisor
    return _val

_loopsB = find_loop_num(7, _publicB)
_encryptionA = transform_key(_loopsB, _publicA)
# _loopsA = find_loop_num(7, _publicA)
# _encryptionB = transform_key(_loopsA, _publicB)

print(f"PART 1: {_encryptionA}")
