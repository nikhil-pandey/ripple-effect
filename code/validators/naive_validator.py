def naive_validator(grid, cell, value):
    for room_cell in cell.get_room().get_cells():
        if room_cell.get_value() == value:
            return False

    row_seen = [{} for _ in range(grid.get_row_count())]
    col_seen = [{} for _ in range(grid.get_column_count())]
    for r_idx, row in enumerate(grid.get_cells()):
        for c_idx, cell in enumerate(row):
            if not cell.has_value():
                continue

            if cell.get_value() in row_seen[r_idx]:
                if c_idx - row_seen[r_idx][cell.get_value()] <= cell.get_value():
                    print('Already seen this value in the row')
                    return False
            row_seen[r_idx][cell.get_value()] = c_idx

            if cell.get_value() in col_seen[c_idx]:
                if r_idx - col_seen[c_idx][cell.get_value()] <= cell.get_value():
                    print('Already seen the column')
                    return False

            col_seen[c_idx][cell.get_value()] = r_idx

    return True