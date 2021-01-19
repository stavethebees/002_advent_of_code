
def solve(expression):
    _newexpression = []
    _length = len(expression)
    _pos = 0
    while (_pos < _length):
        _char = expression[_pos]
        if _char in ("+", "*"):
            _newexpression.append(_char)
            _pos += 1
            continue
        else:
            if _char.isnumeric():
                _newexpression.append(_char)
            elif _char == "(":
                _matchingbracket = get_matching_bracket_pos(expression, _pos)
                _newexpression.append(solve(expression[_pos + 1: _matchingbracket]))
                _pos += (_matchingbracket - _pos) - 1
            _newexpression.insert(0, "(")
            _newexpression.append(")")

        _pos += 1
    return ''.join(_newexpression)