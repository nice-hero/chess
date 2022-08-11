


import pgntofen # assumes you have pgntofen.py in the same directory, or you know how to handle python modules.

PGNMoves = ['d4','d5']

pgnConverter = pgntofen.PgnToFen()

pgnConverter.move(PGNMoves.split(''))
fen = pgnConverter.getFullFen()


print(fen)
#fen will be 'rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR - KQkq'




















