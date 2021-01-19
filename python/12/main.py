import math

_handle = "test.txt"
_handle = "input.txt"

with open(_handle, 'r') as file:
    _data = [[_[0], int(_[1:])] for _ in file.read().splitlines()]


# wanted to try out classes in this solution
class Ship:
    def __init__(self, x, y, direction=1):
        self.x = x
        self.y = y
        self.orientation = direction
        self.frame_dict = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
        self.orientation_dict = {0: "N", 1: "E", 2: "S", 3: "W"}
        self.turns_dict = {"L": -1, "R": 1}

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def turn(self, amount):
        self.orientation += (amount // 90)
        self.orientation %= 4

    def execute_instruction(self, instruction, amount):
        if instruction in "NEWS":
            _dx = self.frame_dict[instruction][0] * amount
            _dy = self.frame_dict[instruction][1] * amount
            self.move(_dx, _dy)

        elif instruction in "LR":
            _dw = self.turns_dict[instruction] * amount
            self.turn(_dw)

        elif instruction == "F":
            _instruction = self.orientation_dict[self.orientation]
            self.execute_instruction(_instruction, amount)

    def get_manhattan_dist(self):
        return abs(self.x) + abs(self.y)


class ShipWithWaypoint(Ship):
    def __init__(self, x, y, waypointx, waypointy):
        Ship.__init__(self, x, y)
        self.waypointx = waypointx
        self.waypointy = waypointy

    def move_waypoint(self, x, y):
        self.waypointx += x
        self.waypointy += y

    def set_waypoint(self, x, y):
        self.waypointx = x
        self.waypointy = y

    def rotate_waypoint(self, amount):
        _amount = -math.radians(amount)
        _cosvalue = math.cos(_amount)
        _sinvalue = math.sin(_amount)
        _newx = round(self.waypointx * _cosvalue -
                      self.waypointy * _sinvalue, 5)
        _newy = round(self.waypointx * _sinvalue +
                      self.waypointy * _cosvalue, 5)
        self.set_waypoint(_newx, _newy)

    def execute_instruction(self, instruction, amount):
        if instruction in "NEWS":
            _dx = self.frame_dict[instruction][0] * amount
            _dy = self.frame_dict[instruction][1] * amount
            self.move_waypoint(_dx, _dy)

        elif instruction in "LR":
            _dw = self.turns_dict[instruction] * amount
            self.rotate_waypoint(_dw)

        elif instruction == "F":
            _offsetx = self.waypointx * amount
            _offsety = self.waypointy * amount
            self.move(_offsetx, _offsety)


def pt1(data):
    ship = Ship(0, 0, direction=1)
    for _list in data:
        _instruction = _list[0]
        _value = _list[1]
        ship.execute_instruction(_instruction, _value)
    return ship.get_manhattan_dist()


def pt2(data):
    shipwp = ShipWithWaypoint(0, 0, 10, 1)
    for _list in data:
        _instruction = _list[0]
        _value = _list[1]
        shipwp.execute_instruction(_instruction, _value)
    return int(shipwp.get_manhattan_dist())


print(f"PART 1: {pt1(_data)}")
print(f"PART 2: {pt2(_data)}")