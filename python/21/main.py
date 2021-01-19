import re
_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [_ for _ in file.read().splitlines()]

_regex_ingredients = r".*(?=\s\()"
_regex_allergens = r"(?<=contains\s).*(?=\))"
_ingredients = [set(re.search(_regex_ingredients, _x).group(0).split()) for _x in _data]
_allergens = [set(re.search(_regex_allergens, _x).group(0).split(", ")) for _x in _data]

_all_allergens = {_allergen for _sublist in _allergens for _allergen in _sublist}
_all_ingredients = {_ingredient for _sublist in _ingredients for _ingredient in _sublist}

_allergen = ""
_common_ingredient = ""
_dangerous_ingredients = []
_dangerous_allergens = []

while(sum(map(len,_allergens)) > 0):
    for _a in _all_allergens:
        _common_ids = [_idx for _idx, _line in enumerate(_allergens) if _a in _line]
        _common_ingredients = _all_ingredients
        for _i in _common_ids:
            _this_ingredients = _ingredients[_i]
            _common_ingredients = _common_ingredients.intersection(_this_ingredients)

        if len(_common_ingredients) == 1:
            _allergen = _a
            _common_ingredient = _common_ingredients.pop()
            _dangerous_ingredients.append(_common_ingredient)
            _dangerous_allergens.append(_allergen)
            break

    for _idx, _ingredient in enumerate(_ingredients):
        if _common_ingredient in _ingredient:
            _ingredient.remove(_common_ingredient)
            _allergenlist = _allergens[_idx]
            _allergenlist.discard(_allergen)
            _allergens[_idx] = _allergenlist

print(f"PART 1: {sum(map(len,_ingredients))}")
print(f"PART 2: {','.join([_x for _,_x in sorted(zip(_dangerous_allergens,_dangerous_ingredients))])}")