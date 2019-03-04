def human_like_next_move(cell):
    """
    Human like next move. Returns the next move if a move has been
    prioritized. Else falls back to the default sequence.
    :param cell: The cell.
    :return: next moves for the cell.
    """
    next_move = cell.next_move

    if next_move is None:
        for value in cell.possible_moves:
            yield value
        return

    yield next_move
