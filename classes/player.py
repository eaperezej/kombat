from typing import List
from classes.keymap import KeyAction, KeyMaps

DEFAULT_PLAYER_LIFE: int = 6


class Player:
    name: str
    life: int
    movements: List[str]
    actions: List[str]
    keymaps: KeyMaps

    def __init__(
        self,
        *,
        name: str,
        life: int = DEFAULT_PLAYER_LIFE,
        movements: List[str],
        actions: List[str],
        keymaps: KeyMaps
    ) -> None:
        self.name = name
        self.life = life if life > 0 else DEFAULT_PLAYER_LIFE
        self.movements = movements
        self.actions = actions
        self.keymaps = keymaps

    def is_alive(self) -> bool:
        return self.life > 0

    def recv_hit(self, *, damage: int) -> None:
        self.life -= damage

    @property
    def map_actions(self) -> List[KeyAction]:
        mlen = len(self.movements)
        mactions = [(self.movements[i], self.actions[i]) for i in range(mlen)]
        actions_bag = []

        for action in mactions:
            for index in range(-3, 0):
                first_chain = action[0][index:]
                first_test = (first_chain, action[1])
                if first_test in self.keymaps:
                    actions_bag.append(self.keymaps[first_test])
                    break

        return actions_bag
