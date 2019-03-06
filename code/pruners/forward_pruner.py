def forward_pruner(grid, cell):
    """
    Forward Pruner. Stops search a room has no possible values.
    :param grid: The grid.
    :param cell: The cell that was changed.
    :return: Tuple of removed values and if the search should continue
    """
    removed = []

    # Only for Human-Like MRV
    cell.room.possible_options[cell.value].discard(cell)

    # Prune the values in the same room
    for room_cell in cell.room.cells:
        if cell == room_cell or room_cell.value is not None:
            continue

        if cell.value in room_cell.possible_moves:
            room_cell.possible_moves.discard(cell.value)

            room_cell.room.possible_options[cell.value].discard(room_cell)

            removed.append((room_cell, cell.value))
            if len(room_cell.possible_moves) == 0:
                return removed, False

    # Prune the values in the column
    for c_idx in range(max(0, cell.col - cell.value),
                       min(grid.column_count,
                           cell.col + cell.value + 1)):
        this_cell = grid.cells[cell.row][c_idx]

        if cell == this_cell or this_cell.value is not None:
            continue

        if cell.value in this_cell.possible_moves:
            this_cell.possible_moves.discard(cell.value)

            this_cell.room.possible_options[cell.value].discard(this_cell)

            removed.append((this_cell, cell.value))
            if len(this_cell.possible_moves) == 0:
                return removed, False

    # Prune the values in the column
    for r_idx in range(max(0, cell.row - cell.value),
                       min(grid.row_count,
                           cell.row + cell.value + 1)):
        this_cell = grid.cells[r_idx][cell.col]

        if cell == this_cell or this_cell.value is not None:
            continue

        if cell.value in this_cell.possible_moves:
            this_cell.possible_moves.discard(cell.value)

            this_cell.room.possible_options[cell.value].discard(this_cell)

            removed.append((this_cell, cell.value))
            if len(this_cell.possible_moves) == 0:
                return removed, False

    return removed, True