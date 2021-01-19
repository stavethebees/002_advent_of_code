import re

_handle = "test.txt"
_handle = "input.txt"


def get_valid_ranges_set(range_rules):
    _valid_ranges = set()
    for _range in range_rules:
        _result = re.search(r"(\d+)-(\d+)\sor\s(\d+)-(\d+)", _range)
        _loA, _hiA, _loB, _hiB = list(map(int, _result.groups()))
        _valid_ranges.update(range(_loA, _hiA + 1))
        _valid_ranges.update(range(_loB, _hiB + 1))
    return _valid_ranges


def get_valid_ranges_dict(range_rules):
    _valid_ranges = {}
    for idx, _range in enumerate(range_rules):
        _result = re.search(r"(\d+)-(\d+)\sor\s(\d+)-(\d+)", _range)
        _loA, _hiA, _loB, _hiB = list(map(int, _result.groups()))
        _valid_ranges[idx] = set(
            [*range(_loA, _hiA + 1), *range(_loB, _hiB + 1)])
    return _valid_ranges


def create_index_to_field_map(range_rules):
    _map = {}
    for _idx, _range in enumerate(range_rules):
        _result = re.search(r"(.+)(?=:)", _range).group(0)
        _map[_idx] = _result
    return _map


def calc_error_rate(range_rules, nearbytickets):
    _valid_ranges = get_valid_ranges_set(range_rules)
    return sum(filter(lambda _: _ not in _valid_ranges, nearbytickets))


def remove_invalid_tickets(nearby, range_rules):
    _valid_ranges = get_valid_ranges_set(range_rules)
    _num_fields = len(range_rules)
    _nearby_separated_tickets = []
    for num in range(0, len(nearby), _num_fields):
        _current_ticket = nearby[num: num + _num_fields]
        if all([i in _valid_ranges for i in _current_ticket]):
            _nearby_separated_tickets.append(_current_ticket)
    return _nearby_separated_tickets


def calc_sum_with_fields(range_rules, nearby, myticket, startswith):
    _num_fields = len(range_rules)
    _valid_tickets = remove_invalid_tickets(nearby, range_rules)
    _index_to_field = create_index_to_field_map(range_rules)
    _valid_ranges_dict = get_valid_ranges_dict(range_rules)

    # transpose valid tickets so can go through by index
    _valid_tickets_transposed = list(map(list, zip(*_valid_tickets)))
    _candidate_dict = {k: set(range(0, _num_fields))
                       for k in range(_num_fields)}
    for _index, _item in enumerate(_valid_tickets_transposed):
        for _num in _item:
            for _i in range(_num_fields):
                if _num not in _valid_ranges_dict[_i]:
                    _candidate_dict[_index].remove(_i)

    # go thru candidate dictionary and remove recurring with set difference operation
    _sorted_candidate_list = [[k, v] for k, v in sorted(_candidate_dict.items(), key=lambda x: len(x[1]))]
    _counter = 0
    _prev_set = {}
    while (_counter < _num_fields):
        _, _set = _sorted_candidate_list[_counter]
        _sorted_candidate_list[_counter][1] = _set.difference(_prev_set)
        _prev_set = _set
        _counter += 1

    _sorted_candidate_dict = {i[0]: min(i[1]) for i in _sorted_candidate_list}
    _myticket_dict = {_index_to_field[_sorted_candidate_dict[_idx]]: k for _idx, k in enumerate(myticket)}
    _sum = 1
    for k, v in _myticket_dict.items():
        if k.startswith(startswith):
            _sum *= v
    return _sum


with open(_handle, 'r') as file:
    _lines = [l for l in file.read().splitlines() if l != ""]
    _range_rules = _lines[:_lines.index("your ticket:")]
    _nearby = ",".join(_lines[_lines.index("nearby tickets:") + 1:])
    _nearby = [int(i) for i in _nearby.split(",")]
    _myticket = _lines[_lines.index("your ticket:") + 1]
    _myticket = [int(i) for i in _myticket.split(",")]


_pt1 = calc_error_rate(_range_rules, _nearby)
print(f"PART 1: {_pt1}")

_pt2 = calc_sum_with_fields(_range_rules, _nearby, _myticket, "departure")
print(f"PART 2: {_pt2}")
