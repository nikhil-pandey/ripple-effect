def default_next_move(cell):
    """
    Default next move. Returns the set from the cell without any special
    comparisons.
    :param cell: The cell.
    :return: The default set of moves.
    """
    next_move = cell.next_move

    if next_move is None:
        for value in cell.possible_moves:
            yield value
        return

    yield next_move