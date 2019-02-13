def naive_validator(grid, cell, value):
    for room in grid.get_rooms():
        for room_cell in room.get_cells():
            if room_cell.value == value:
                return False

    row_seen = [{} for _ in range(grid.get_row_count())]
    col_seen = [{} for _ in range(grid.get_column_count())]
    for r_idx, row in enumerate(grid.get_cells()):
        for c_idx, cell in enumerate(row):
            if not cell.has_value():
                continue

            if cell.value in row_seen[r_idx]:
                if c_idx - row_seen[r_idx][cell.value] <= cell.value:
                    return False
            row_seen[r_idx][cell.value] = c_idx

            if cell.value in col_seen[c_idx]:
                if r_idx - col_seen[c_idx][cell.value] <= cell.value:
                    return False

            col_seen[c_idx][cell.value] = r_idx

    return True


def localized_validator(grid, cell, value):
    for room_cell in cell.get_room().get_cells():
        if not room_cell.has_value() or cell == room_cell:
            continue

        if room_cell.get_value() == value:
            return False

    for c_idx in range(max(0, cell.get_column() - value),
                       min(grid.get_column_count(), cell.get_column() + value + 1)):
        if c_idx != cell.get_column() and \
                value == grid.get_cell(cell.get_row(), c_idx).get_value():
            return False

    for r_idx in range(max(0, cell.get_row() - value),
                       min(grid.get_row_count(), cell.get_row() + value + 1)):
        if r_idx != cell.get_row() and \
                value == grid.get_cell(r_idx, cell.get_column()).get_value():
            return False

    return True
