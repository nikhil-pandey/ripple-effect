import logging


def human_like_next_move(cell):
    next_move = cell.get_next_move()

    if next_move is None:
        for value in cell.get_moves():
            yield value
        return

    # logging.debug('MOVE: Selecting prioritized Move: %d for %s' % (next_move, cell))
    yield next_move
