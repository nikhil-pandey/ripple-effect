def patch_removed_values(items, cell):
    """
    Patch back the removed values.
    :param items: Tuple of cell and removed value
    :param cell: The cell that was processed.
    :return: None
    """
    # Only for Human-Like MRV
    cell.room.possible_options[cell.value].add(cell)
    
    for cell, val in items:
        cell.room.possible_options[val].add(cell)
        cell.possible_moves.add(val)
