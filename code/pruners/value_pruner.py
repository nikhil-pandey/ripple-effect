import logging


def value_pruner(grid, cell):
    """
    Value Pruner. Like Forward Pruner but doesn't stop search.
    :param grid: The grid.
    :param cell: The cell that was changed.
    :return: Tuple of removed values and if the search should continue
    """
    # logging.debug('PRUNER: Using value pruner to prune %s :)' % (cell))
    removed = []
    for room_cell in cell.get_room().get_cells():
        if cell == room_cell or room_cell.has_value():
            continue

        if cell.get_value() in room_cell.get_moves():
            # logging.debug('PRUNER: Pruning value %s from %s' % (cell.get_value(), room_cell))
            room_cell.remove_move(cell.get_value())
            room_cell.get_room().remove_move(cell.get_value(), room_cell)
            removed.append((room_cell, cell.get_value()))

    for c_idx in range(max(0, cell.get_column() - cell.get_value()),
                       min(grid.get_column_count(), cell.get_column() + cell.get_value() + 1)):
        this_cell = grid.get_cell(cell.get_row(), c_idx)

        if cell == this_cell or this_cell.has_value():
            continue

        if cell.get_value() in this_cell.get_moves():
            # logging.debug('PRUNER: Pruning value %s from %s' % (cell.get_value(), this_cell))
            this_cell.remove_move(cell.get_value())
            this_cell.get_room().remove_move(cell.get_value(), this_cell)
            removed.append((this_cell, cell.get_value()))

    for r_idx in range(max(0, cell.get_row() - cell.get_value()),
                       min(grid.get_row_count(), cell.get_row() + cell.get_value() + 1)):
        this_cell = grid.get_cell(r_idx, cell.get_column())

        if cell == this_cell or this_cell.has_value():
            continue

        if cell.get_value() in this_cell.get_moves():
            # logging.debug('PRUNER: Pruning value %s from %s' % (cell.get_value(), this_cell))
            this_cell.remove_move(cell.get_value())
            this_cell.get_room().remove_move(cell.get_value(), this_cell)
            removed.append((this_cell, cell.get_value()))

    return removed, True
