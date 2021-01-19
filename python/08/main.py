_handle = "test.txt"
_handle = "input.txt"


with open(_handle, 'r') as file:
    _data = [_ for _ in file.read().splitlines()]


def process_input(data):
    _processed = []
    for _item in data:
        _i = _item.split(" ")
        _list = [_i[0], int(_i[1])]
        _processed.append(_list)
    return _processed


def swap_instruction(instruction):
    _map = {"nop": "jmp", "jmp": "nop"}
    _instruction = instruction[0]
    if _instruction in _map.keys():
        instruction[0] = _map[_instruction]
    return instruction


def run_instructions(instructions):
    _data = [_[:] for _ in instructions]  # make local copy of list
    _acc = 0
    _pos = 0
    _length = len(_data)
    _break = False
    _visited = [False] * _length  # list to keep track of visited

    while(_pos < _length):
        if _visited[_pos]:
            _break = True
            break

        _visited[_pos] = True
        _instruction = _data[_pos][0]
        _inc_val = _data[_pos][1]

        if _instruction == "acc":
            _acc += _inc_val

        elif _instruction == "jmp":
            _pos += _inc_val
            continue

        _pos += 1
    return _break, _acc


def permute_and_loop(input):
    _acc = 0
    for _instruction in input:
        _orig_instruction = _instruction[0]
        swap_instruction(_instruction)
        _result_tuple = run_instructions(input)
        if _result_tuple[0] == False:
            return _result_tuple[1]
        # set back to orig instruction for next iteration
        _instruction[0] = _orig_instruction
    return _acc


_instructions = process_input(_data)
print(f"PART 1: {run_instructions(_instructions)[1]}")
print(f"PART 2: {permute_and_loop(_instructions)}")
