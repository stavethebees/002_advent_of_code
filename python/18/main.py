_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as _file:
    _data = []
    for _ in _file.read().splitlines():
        _data.append(_)


def get_matching_bracket_pos(expression, pos):
    _counter = 1
    _pos = pos
    _char = expression[pos]
    if _char not in [")", "("]:
        return pos # if this char isnt a bracket just return same pos
    
    _oppositebracket = {"(":")", ")":"("}
    _increment = {"(": 1, ")": -1}
    while(_counter > 0):
        _pos += _increment[_char]
        if expression[_pos] == _char:
            _counter += 1
        elif expression[_pos] == _oppositebracket[_char]:
            _counter -= 1
    return _pos


def add_bracket(expression, pos, side):
    _bracket_pos = get_matching_bracket_pos(expression, pos)
    _expression = list(expression)
    if side == "right":
        _bracket_pos += 1
    _oppositebracket = {"left": "(", "right": ")"}
    _expression.insert(_bracket_pos, _oppositebracket[side])
    return _expression


def solve(expression, advanced=False):
    _expression = list(expression)
    _pos = 0
    _length = len(expression)

    while _pos < _length:
        _char = _expression[_pos]
        _length = len(_expression)
        if advanced and _char == "*":
            _pos += 1
            continue
        if _char == "+" or _char == "*":
            _left_term = add_bracket(_expression, _pos - 1, "left")[:_pos + 1]
            _right_term = add_bracket(_expression, _pos + 1, "right")[_pos + 1:]
            _expression = _left_term
            _expression.extend(_char)
            _expression.extend(_right_term)
            _pos += 1
        _pos += 1
    
    return ''.join(_expression)


def evaluate_expression(expression, advanced=False):
    return eval(solve(expression.replace(' ', ''), advanced))


print(f"PART 1: {sum(map(lambda x:evaluate_expression(x), _data))}")
print(f"PART 2: {sum(map(lambda x:evaluate_expression(x, advanced=True), _data))}")