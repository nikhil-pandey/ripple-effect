import logging


def default_next_move(cell):
    # logging.debug('MOVE: Default moves, no priority')
    return cell.get_moves()
