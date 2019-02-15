def naive_validator(grid, cell, value):
    for room_cell in cell.get_room().get_cells():
        if room_cell.get_value() == value:
            return False

    cells = grid.get_cells()
    for check_cell in cells[cell.get_row()]:
        if check_cell == cell:
            continue

        if check_cell.get_value() == value and abs(check_cell.get_column() - cell.get_column()) <= value:
            return False

    for i in range(grid.get_row_count()):
        check_cell = cells[i][cell.get_column()]

        if check_cell == cell:
            continue

        if check_cell.get_value() == value and abs(i - cell.get_row()) <= value:
            return False

    return True