import re
from collections import namedtuple

_handle = 'test.txt'
_handle = 'input.txt'

with open(_handle, 'r') as file:
    _input = file.read()
    _split = re.split(r'\n(?=mask)', _input)
    _data = [_.split('\n') for _ in _split]


def process_input(data):
    # gonna try out named tuples
    Instruction = namedtuple('Instruction', ('address', 'value'))
    Entry = namedtuple('Entry', ['mask', 'instructions'])

    _entries = []
    for _item in data:
        _mask = _item[0].split()[-1]
        _instructionlist = []
        for _i in _item[1:]:
            _instruction = re.findall(r'(?<=\[)\d+', _i)[0]
            _value = _i.split()[-1]
            _instructionlist.append(Instruction(_instruction, int(_value)))
        _entries.append(Entry(_mask, _instructionlist))
    return _entries


def pt1(entries):
    _memory = dict()
    for _entry in entries:
        for _instruction in _entry.instructions:
            _result = ''.join(map(lambda x, y: y if x == 'X' else x,
                                  _entry.mask, format(_instruction.value, '036b')))
            _num = int(_result, 2)
            _memory[_instruction.address] = _num
    return sum(_memory.values())


def apply_bitmask(address, mask):
    return "".join(map(lambda x, y: y if y in ("X", "1") else x, address, mask))


def generate_address_permutations(address):
    _count = address.count("X")
    _formatstring = "0" + str(_count) + "b"

    # generate list of binary permutations
    _binary_permutations = [format(i, _formatstring) for i in range(2**_count)]

    # plug permutations into their corresponding X's
    _permuations = []
    for b in _binary_permutations:
        _idx = 0
        _newaddress = ""
        for i in address:
            if i == "X":
                _newaddress += b[_idx]
                _idx += 1
            else:
                _newaddress += i
        _permuations.append(int(_newaddress, 2))
    return _permuations


def pt2(entries):
    _memory = dict()
    for _entry in entries:
        for _instruction in _entry.instructions:
            _address = format(int(_instruction.address), '036b')
            _result = apply_bitmask(_address, _entry.mask)
            _addresses = generate_address_permutations(_result)
            for _fetchedaddress in _addresses:
                _memory[_fetchedaddress] = _instruction.value
    return sum(_memory.values())


_entries = process_input(_data)
print(f"PART 1: {pt1(_entries)}")
print(f"PART 2: {pt2(_entries)}")