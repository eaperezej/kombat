import pytest
from classes.game import Game
from classes.logging import GameLog
from classes.player import Player
from classes.keymap import RIGHT_ACTIONS_KEYMAPS, LEFT_ACTIONS_KEYMAPS


@pytest.fixture()
def player_1() -> Player:
    movements = ["D", "DSD", "S", "DSD", "SD"]
    actions = ["K", "P", "", "K", "P"]
    name = "player_1"
    p = Player(
        name=name,
        movements=movements,
        actions=actions,
        keymaps=RIGHT_ACTIONS_KEYMAPS,
    )

    return p


@pytest.fixture()
def player_2() -> Player:
    movements = ["SA", "SA", "SA", "ASA", "SA"]
    actions = ["K", "", "K", "P", "P"]
    name = "player_2"
    p = Player(
        name=name,
        movements=movements,
        actions=actions,
        keymaps=LEFT_ACTIONS_KEYMAPS,
    )

    return p


def test_game(player_1: Player, player_2: Player):
    g = Game(
        player_1=player_1,
        player_2=player_2,
        log=GameLog()
    )
    g.start()

    result_log = [
        "Turno 1: player_1 retrocede y lanza una patada",
        "Turno 1: player_2 conecta un REMEYUKEN",
        "Turno 2: player_1 conecta un TALADOKEN",
        "Turno 2: player_2 conecta un REMEYUKEN",
        "player_2 gana la partida"
    ]

    assert not player_1.is_alive()
    assert player_2.is_alive()
    assert g.get_game_trace() == result_log
