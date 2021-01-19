import re

_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [_ for _ in file.read().splitlines()]


def process_data_pt1(data):
    _bags = dict()
    _regex_key = r"(\sbags?[,.]?(\scontain)?(\sno\sother)?)|\s\d"
    for _line in data:
        _line = re.sub(_regex_key, r"", _line)
        _matches = re.findall(r"\w+\s\w+", _line)
        if len(_matches) > 1:
            _bags[_matches[0]] = set(_matches[1:])
    return _bags


def process_data_pt2(data):
    _bags = dict()
    _regex_key = r"(\sbags\scontain\s)"
    for _line in _data:
        _split = re.split(_regex_key, _line)
        _bag = _split[0]
        _groups = re.findall(r"(\d)\s(\w+\s\w+)", _split[-1])
        if len(_groups) != 0:
            _bags[_bag] = _groups
        else:
            _bags[_bag] = None
    return _bags


def solve_pt1(bags, search_bag):
    _matches = set()
    def find_bag(bag):
        for _bag, _contains in bags.items():
            if _bag not in _matches and bag in _contains:
                _matches.add(_bag)
                find_bag(_bag)
    find_bag(search_bag)
    return len(_matches)


def solve_pt2(bags, search_bag):
    _sum = 1
    def find_num(bag):
        if bags[bag] is None:
            return 0
        else:
            _list = []
            for _entry in bags[bag]:
                _mult = int(_entry[0])
                _list.append(_mult)
                _sum = _mult * find_num(_entry[1])
                _list.append(_sum)
            return sum(_list)
    _sum = find_num(search_bag)
    return _sum


_bags_simple = process_data_pt1(_data)
_bags_adv = process_data_pt2(_data)

print(f"PART 1: {solve_pt1(_bags_simple, 'shiny gold')}")
print(f"PART 2: {solve_pt2(_bags_adv, 'shiny gold')}")