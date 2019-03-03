def naive_validator(grid, cell, value):
    """
    Naive validator.
    :param grid: The grid.
    :param cell: The cell to change.
    :param value: The new value.
    :return: True if validation passed else False
    """
    for room_cell in cell.room.cells:
        if room_cell.value == value:
            return False

    cells = grid.cells
    for check_cell in cells[cell.row]:
        if check_cell == cell:
            continue

        if check_cell.value == value and abs(
                check_cell.col - cell.col) <= value:
            return False

    for i in range(grid.row_count):
        check_cell = cells[i][cell.col]

        if check_cell == cell:
            continue

        if check_cell.value == value and abs(
                i - cell.row) <= value:
            return False

    return True
