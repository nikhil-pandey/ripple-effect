def default_next_move(cell):
    """
    Default next move. Returns the set from the cell without any special
    comparisons.
    :param cell: The cell.
    :return: The default set of moves.
    """
    return cell.possible_moves
