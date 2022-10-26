from typing import List
from classes.logging import GameLog
from classes.player import Player


class Game:
    player_1: Player
    player_2: Player
    log: GameLog

    def __init__(
        self,
        player_1: Player,
        player_2: Player,
        log: GameLog
    ) -> None:
        self.player_1 = player_1
        self.player_2 = player_2
        self.log = log

    def _get_priority(self) -> List[Player]:
        order = [self.player_1, self.player_2]

        if len(self.player_2.movements) > len(self.player_1.movements):
            order = [self.player_2, self.player_1]

        return order

    def get_game_trace(self) -> List[str]:
        return self.log.trace()

    def start(self) -> None:
        first_player, second_player = self._get_priority()
        first_player_ma = first_player.map_actions
        second_player_ma = second_player.map_actions
        turn = 0

        while first_player.is_alive() and second_player.is_alive():
            try:
                second_player.recv_hit(damage=first_player_ma[turn].damage)
                self.log.info(
                    f"Turno {turn + 1}: {first_player.name} {first_player_ma[turn].verbose}"  # noqa: 501
                )
            except IndexError:
                continue

            try:
                first_player.recv_hit(damage=second_player_ma[turn].damage)
                self.log.info(
                    f"Turno {turn + 1}: {second_player.name} {second_player_ma[turn].verbose}"  # noqa: 501
                )
            except IndexError:
                continue

            turn += 1

        if first_player.is_alive():
            self.log.info(f"{first_player.name} gana la partida")
        else:
            self.log.info(f"{second_player.name} gana la partida")
