import logging


def default_next_move(cell):
    """
    Default next move. Returns the set from the cell without any special
    comparisons.
    :param cell: The cell.
    :return: The default set of moves.
    """
    # logging.debug('MOVE: Default moves, no priority')
    return cell.get_moves()
