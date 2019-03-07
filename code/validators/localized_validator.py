def localized_validator(grid, cell, value):
    """
    Localized validator.
    :param grid: The grid.
    :param cell: The cell to change.
    :param value: The new value.
    :return: True if validation passed else False
    """
    for region_cell in cell.region.cells:
        if cell == region_cell or region_cell.value is None:
            continue

        if region_cell.value == value:
            return False

    for c_idx in range(max(0, cell.col - value),
                       min(grid.column_count,
                           cell.col + value + 1)):
        if c_idx != cell.col and \
                value == grid.cells[cell.row][c_idx].value:
            return False

    for r_idx in range(max(0, cell.row - value),
                       min(grid.row_count, cell.row + value + 1)):
        if r_idx != cell.row and \
                value == grid.cells[r_idx][cell.col].value:
            return False

    return True
