def localized_validator(grid, cell, value):
    """
    Localized validator.
    :param grid: The grid.
    :param cell: The cell to change.
    :param value: The new value.
    :return: True if validation passed else False
    """
    for room_cell in cell.get_room().get_cells():
        if not room_cell.has_value() or cell == room_cell:
            continue

        if room_cell.get_value() == value:
            return False

    for c_idx in range(max(0, cell.get_column() - value),
                       min(grid.get_column_count(),
                           cell.get_column() + value + 1)):
        if c_idx != cell.get_column() and \
                value == grid.get_cell(cell.get_row(), c_idx).get_value():
            return False

    for r_idx in range(max(0, cell.get_row() - value),
                       min(grid.get_row_count(), cell.get_row() + value + 1)):
        if r_idx != cell.get_row() and \
                value == grid.get_cell(r_idx, cell.get_column()).get_value():
            return False

    return True
