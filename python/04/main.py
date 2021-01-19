import re

_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [i for i in file.read().split("\n\n")]


def process_data(data):
    _list = []
    for _item in data:
        _item = re.split(r"\s", _item)
        _dict = {}
        for _i in _item:
            _l = _i.split(":")
            _dict[_l[0]] = _l[1]
        _list.append(_dict)
    return _list


def pt1(data):
    _validkeys = set(["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"])
    _valid = 0
    for _item in data:
        _item.pop("cid", 0)
        _valid += _validkeys == set(_item.keys())
    return _valid


def pt2(data):
    _valid = 0
    for _item in data:
        _item.pop("cid", "")
        _byr = 1920 <= int(_item.get("byr", 0)) <= 2002
        _iyr = 2010 <= int(_item.get("iyr", 0)) <= 2020
        _eyr = 2020 <= int(_item.get("eyr", 0)) <= 2030
        _hcl = re.match(r"#[0-9a-f]{6}\b", _item.get("hcl", "")) != None
        _hgt = re.match(
            r"(((1[5-8][0-9])|(19[0-3]))cm)|((59|6[0-9]|7[0-6]))in", _item.get("hgt", "")) != None
        _ecl = re.match(r"\b(amb|blu|brn|gry|grn|hzl|oth)\b",
                        _item.get("ecl", "")) != None
        _pid = re.match(r"\d{9}\b", _item.get("pid", "")) != None
        _valid += _byr & _iyr & _eyr & _pid & _hcl & _ecl & _hgt
    return _valid


_masterlist = process_data(_data)
print(f"PART 1: {pt1(_masterlist)}")
print(f"PART 2: {pt2(_masterlist)}")
