from dataclasses import dataclass
from typing import Dict, Tuple


@dataclass
class KeyAction:
    movement: str
    combo: str
    action: str
    damage: int
    verbose: str


KeyMaps = Dict[Tuple[str, ...], KeyAction]


COMMON_MOVEMENTS_KEYMAPS: KeyMaps = {
    ("W", "P"): KeyAction("W", "", "P", 1, "salta y golpea"),
    ("S", "P"): KeyAction("S", "", "P", 1, "agacha y golpea"),
    ("W", "K"): KeyAction("W", "", "K", 1, "salta y da una patada"),
    ("S", "K"): KeyAction("S", "", "K", 1, "agacha y da una patada"),
    ("", "P"): KeyAction("", "", "P", 1, "golpea"),
    ("", "K"): KeyAction("", "", "K", 1, "patea"),
}

LEFT_ACTIONS_KEYMAPS: KeyMaps = {
    **COMMON_MOVEMENTS_KEYMAPS,
    ("SA", "K"): KeyAction("SA", "REMEYUKEN", "K", 3, "conecta un REMEYUKEN"),
    ("ASA", "P"): KeyAction("ASA", "TALADOKEN", "P", 2, "conecta un TALADOKEN"),  # noqa: 501
    ("A", "P"): KeyAction("A", "", "P", 1, "retrocede y lanza un golpe"),
    ("A", "K"): KeyAction("A", "", "K", 1, "retrocede y lanza una patada"),
    ("D", "P"): KeyAction("D", "", "P", 1, "avanza y lanza un golpe"),
    ("D", "K"): KeyAction("D", "", "K", 1, "avanza y lanza una patada"),
}

RIGHT_ACTIONS_KEYMAPS: KeyMaps = {
    **COMMON_MOVEMENTS_KEYMAPS,
    ("DSD", "P"): KeyAction("DSD", "TALADOKEN", "P", 3, "conecta un TALADOKEN"),  # noqa: 501
    ("SD", "K"): KeyAction("SD", "REMEYUKEN", "K", 2, "conecta un REMEYUKEN"),
    ("A", "P"): KeyAction("A", "", "P", 1, "avanza y lanza un golpe"),
    ("A", "K"): KeyAction("A", "", "K", 1, "avanza y lanza una patada"),
    ("D", "P"): KeyAction("D", "", "P", 1, "retrocede y lanza un golpe"),
    ("D", "K"): KeyAction("D", "", "K", 1, "retrocede y lanza una patada"),
}
