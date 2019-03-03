def patch_removed_values(items):
    """
    Patch back the removed values.
    :param items: Tuple of cell and removed value
    :return: None
    """
    for cell, val in items:
        cell.room.possible_options[val].add(cell)
        cell.possible_moves.add(val)
