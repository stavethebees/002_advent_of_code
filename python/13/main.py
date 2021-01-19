from math import ceil

_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [_ for _ in file.read().splitlines()]


def pt1(earliest, buses):
    _bus_dict = {i: ceil(earliest/i) * i for i in buses}
    _inv_bus_dict = {v: k for k, v in _bus_dict.items()}
    _list = list(_bus_dict.values())
    _firstid = sorted(_list)[0]
    return (_firstid - earliest) * _inv_bus_dict[_firstid]


# this took quite some time to figure out, the naive brute force method took too long
def pt2(bus_tuples):
    _master_t = _bus_tuples[0][1]
    _offset = 1
    for _position, _bus in bus_tuples:
        while (_master_t + _position) % _bus != 0:
            # skip master_t by offset till we get next valid master t upto this bus
            _master_t += _offset
        # once we find a valid master t (upto current bus), multiply it by the bus id
        # to ensure it keeps the consecutive correct modulo results for all previous buses
        _offset *= _bus

    return _master_t


_bus_list_unprocessed = _data[1].split(",")
_earliest = int(_data[0])
_buses = [int(i) for i in _bus_list_unprocessed if i != "x"]
_bus_tuples = [(i, int(j)) for i, j in enumerate(_bus_list_unprocessed) if j != "x"]

print(f"PART 1: {pt1(_earliest, _buses)}")
print(f"PART 2: {pt2(_bus_tuples)}")