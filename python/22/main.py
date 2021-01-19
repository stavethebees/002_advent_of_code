import re
from collections import deque
_handle = "test.txt"
_handle = "input.txt"

_regex = r"Player\s\d:"
with open(_handle, 'r') as file:
    _data = re.split(_regex, file.read())
    _p1 = deque(map(int, _data[1].split()))
    _p2 = deque(map(int, _data[2].split()))

class Game:
    def __init__(self, p1cards, p2cards):
        self._p1cards = p1cards
        self._p2cards = p2cards
        self.performedmoves = set()
        self.winner = -1

    def playturn(self, adv=False):
        _card1 = self._p1cards.popleft()
        _card2 = self._p2cards.popleft()
        _subwinner = -1
        if adv:
            _lenp1 = len(self._p1cards)
            _lenp2 = len(self._p2cards)
            if _card1 <= _lenp1 and _card2 <= _lenp2:
                _p1copy = self._p1cards.copy()
                _p2copy = self._p2cards.copy()
                _p1, _p2 = deque(), deque()
                for _ in range(_card1):
                    _p1.append(_p1copy.popleft())
                for _ in range(_card2):
                    _p2.append(_p2copy.popleft())

                # play sub game
                _subgame = Game(_p1, _p2)
                while _subgame.winner < 0:
                    _subgame.playturn(adv=True)
                _subwinner = _subgame.winner
                if _subwinner == 1:
                    self._p1cards.append(_card1)
                    self._p1cards.append(_card2)
                else:
                    self._p2cards.append(_card2) 
                    self._p2cards.append(_card1)                    

        if _card1 > _card2 and _subwinner < 0:
            self._p1cards.append(_card1)
            self._p1cards.append(_card2)
        elif _card2 > _card1 and _subwinner < 0:
            self._p2cards.append(_card2) 
            self._p2cards.append(_card1)

        _thishand = ''.join(map(str,self._p1cards))
        if _thishand in self.performedmoves:
            self.winner = 1
            return self.winner

        self.performedmoves.add(_thishand)
        if len(self._p1cards) == 0:
            self.winner = 2
        elif len(self._p2cards) == 0:
            self.winner = 1

        return self.winner

    def calc_winner_score(self):
        _winner = (self._p1cards, self._p2cards)[self.winner - 1]
        return sum([(_idx + 1) * _card for _idx, _card in enumerate(reversed(_winner))])


_p1copy = _p1.copy()
_p2copy = _p2.copy()

_game = Game(_p1, _p2)
while _game.winner < 0:
    _game.playturn()

_game_adv = Game(_p1copy, _p2copy)
while _game_adv.winner < 0:
    _game_adv.playturn(adv=True)

print(f"PART 1: {_game.calc_winner_score()}")
print(f"PART 2: {_game_adv.calc_winner_score()}")