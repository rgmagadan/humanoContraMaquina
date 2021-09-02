#!/usr/bin/env python3

import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("stockfish")
board = chess.Board()

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    print(result.move)
    board.push_san(input("Tu turno: "))

engine.quit()