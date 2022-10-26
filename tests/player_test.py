from classes.keymap import RIGHT_ACTIONS_KEYMAPS, KeyAction
from classes.player import DEFAULT_PLAYER_LIFE, Player
import pytest


@pytest.fixture()
def player() -> Player:
    movements = ["D", "DSD", "S"]
    actions = ["K", "P", "K"]
    name = "player_1"
    p = Player(
        name=name,
        movements=movements,
        actions=actions,
        keymaps=RIGHT_ACTIONS_KEYMAPS,
    )

    return p


def test_init_player() -> None:
    movements = ["D", "DSD", "S", "DSD", "SD"]
    actions = ["K", "P", "", "K", "P"]
    name = "player_1"
    p = Player(
        name=name,
        movements=movements,
        actions=actions,
        keymaps=RIGHT_ACTIONS_KEYMAPS,
    )

    assert p.movements == movements
    assert p.name == name
    assert p.actions == actions
    assert p.keymaps == RIGHT_ACTIONS_KEYMAPS
    assert p.life == DEFAULT_PLAYER_LIFE


def test_map_actions_player(player: Player) -> None:
    action_1 = KeyAction("D", "", "K", 1, "retrocede y lanza una patada")
    action_2 = KeyAction("DSD", "TALADOKEN", "P", 3, "conecta un TALADOKEN")
    action_3 = KeyAction("S", "", "K", 1, "agacha y da una patada")
    result_list_actions = [action_1, action_2, action_3]

    assert player.map_actions == result_list_actions
