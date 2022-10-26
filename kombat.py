import sys
import json
from classes.game import Game
from classes.keymap import LEFT_ACTIONS_KEYMAPS, RIGHT_ACTIONS_KEYMAPS
from classes.logging import GameLog

from classes.player import Player

if __name__ == "__main__":
    filename = "".join(sys.argv[1:])

    with open(filename) as file:
        content = file.read()

    game_config = json.loads(content)

    player_1 = Player(
        name="player_1",
        movements=game_config["player1"]["movimientos"],
        actions=game_config["player1"]["golpes"],
        keymaps=RIGHT_ACTIONS_KEYMAPS
    )

    player_2 = Player(
        name="player_2",
        movements=game_config["player2"]["movimientos"],
        actions=game_config["player2"]["golpes"],
        keymaps=LEFT_ACTIONS_KEYMAPS
    )

    game = Game(
        player_1=player_1,
        player_2=player_2,
        log=GameLog()
    )
    game.start()
    trace = game.get_game_trace()

    for event in trace:
        print(event)
