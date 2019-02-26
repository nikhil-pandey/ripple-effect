def patch_removed_values(items):
    """
    Patch back the removed values.
    :param items: Tuple of cell and removed value
    :return: None
    """
    for cell, val in items:
        cell.get_room().add_move(val, cell)
        cell.add_move(val)
