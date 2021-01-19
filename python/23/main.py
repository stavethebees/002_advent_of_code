_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _cuplist = [int(_num)for _num in file.read()]

_cupdict = dict()
# each cup keeps track of its parent and child 
for _idx, _cup in enumerate(_cuplist):
    _cupdict[_cup] = (_cuplist[(_idx - 1) % len(_cuplist)], _cuplist[(_idx + 1) % len(_cuplist)])


def take_out_cups(cups, cup):
    _nextcup = cup
    _parent, _child = cups[cup]
    for _ in range(3):
        __, _nextcup = cups[_nextcup]
    cups[_parent] = cups[_parent][0], _nextcup
    _orig_parent, _orig_child = cups[_nextcup]
    cups[_nextcup] = _parent, _orig_child


def put_in_cups(cups, in_cup, destination_cup):
    _destination_cup_parent, _destination_cup_child = cups[destination_cup]
    cups[destination_cup] = _destination_cup_parent, in_cup # change child of destination cup to in cup
    _orig_parent, _orig_child = cups[in_cup]
    cups[in_cup] = destination_cup, _orig_child # change in cup's parent to destination cup
    _nextcup = in_cup
    for _ in range(2):
        __, _nextcup = cups[_nextcup]
    _orig_parent, _orig_child = cups[_nextcup]
    cups[_nextcup] = _orig_parent, _destination_cup_child # change last inserted cup's child
    _, _orig_child = cups[_destination_cup_child]
    cups[_destination_cup_child] = _nextcup, _orig_child # change parent of cup after all inserted cups


def find_destination_cup(cups, cup, maxcups):
    _exclude = set()
    _nextcup = cup
    for _ in range(3):
        _parent, _nextcup = cups[_nextcup]
        _exclude.add(_nextcup)
    _destination = cup - 1
    while _destination not in cups or _destination in _exclude or _destination == 0:
        _destination -= 1
        _destination %= maxcups     
    return _destination


def solve(cups, first_cup, moves = 100, adv=False):
    _max_cups = len(cups) + 1
    _current_cup = first_cup
    _finalarrangement = []
    for _ in range(moves):
        _, _next_cup = cups[_current_cup]
        _destination_cup = find_destination_cup(cups, _current_cup, _max_cups)
        take_out_cups(cups, _next_cup)
        put_in_cups(cups, _next_cup, _destination_cup)
        _, _current_cup = cups[_current_cup]
    _, _child_cup = cups[1]

    if adv:
        _cup1 = cups[1][1]
        _cup2 = cups[_cup1][1] 
        _result = _cup1 * _cup2
    else: 
        while _child_cup != 1:
            _finalarrangement.append(_child_cup)
            _, _child_cup = cups[_child_cup]
        _result = ''.join(map(str, _finalarrangement))
    return _result


def populate_cups(cups, init_cup_list, numbers):
    _maxcup = max(cups)
    _lastcup = init_cup_list[-1]

    for _cup in range(_maxcup + 1, numbers + 1):
        cups[_cup] = (_cup - 1, _cup + 1)

    # adjust pointers
    _parent, _child = cups[_lastcup]
    cups[_lastcup] = _parent, _maxcup + 1
    _, _child = cups[_maxcup + 1]
    cups[_maxcup + 1] = _lastcup, _child
    _parent, _child = cups[numbers]
    cups[numbers] = _parent, init_cup_list[0]
    return cups

print(f"PART 1: {solve(_cupdict, _cuplist[0], moves=100)}")
_cupdictorig = _cupdict.copy()
_cupdict = populate_cups(_cupdictorig, _cuplist, 1000000)
print(f"PART 2: {solve(_cupdict, _cuplist[0], moves=10000000, adv=True)}") 
# takes 24 seconds to calculate yikes. gotta move to another algo with iterators 
# instead of creating the whole dictionary of a million