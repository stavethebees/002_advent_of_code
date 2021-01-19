import re

_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = file.read().split("\n\n")
    _messages = _data[-1].splitlines()
    _rules_dict = {i.split(": ")[0]: i.split(": ")[1].strip().replace('"', '') for i in _data[0].splitlines()}

for _k, _list in _rules_dict.items():
    _newlist = _list.split()
    _rules_dict[_k] = _newlist


def solve(rules_dict, messages, start_rule):
    _seen = dict()
    def expand_rule(rule, depth = 0):

        # was going to do recursive regex but not possible with the re module, 
        # so instead limited by recursion depth for part 2
        if depth > 20:
            return ""

        _rule = rules_dict[rule]
        _subrule = []
        if rule in _seen:
            return _seen[rule]
        else:
            if _rule[0].isalpha():
                _seen[rule] = _rule[0]
                return _rule[0]
            else:
                for _r in _rule:
                    if _r == "|":
                        _subrule.append("|")
                    else:
                        _subrule.append("(")
                        _subrule.append(expand_rule(_r, depth + 1))
                        _subrule.append(")")
            _seen[rule] = ''.join(_subrule)
            return ''.join(_subrule)

    _regex = r"\b" + expand_rule(start_rule) + r"\b"
    _regex_compiled = re.compile(_regex)
    return sum([i for i in map(lambda _x: len(re.findall(_regex_compiled, _x)), messages)])


print(f"PART 1: {solve(_rules_dict, _messages, '0')}")

# replace rules
_rules_dict['8'] =  "42 | 42 8".split()
_rules_dict['11'] =  "42 31 | 42 11 31".split()
print(f"PART 2: {solve(_rules_dict, _messages, '0')}")