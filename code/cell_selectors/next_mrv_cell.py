def next_mrv_cell(rooms, cells):
    """
    Selects next move based on minimum remaining values.
    :param rooms: The rooms.
    :param cells: The cells.
    :return: The next cell.
    """
    lowest_count = 0
    lowest_cell = None
    for row in cells:
        for cell in row:
            if cell.value is not None:
                continue
            if lowest_cell is None or len(cell.possible_moves) < lowest_count:
                lowest_count = len(cell.possible_moves)
                lowest_cell = cell
            elif len(cell.possible_moves) == lowest_count:
                # Tie breaker
                # Most tried cells are prioritized first
                if cell.tries > lowest_cell.tries:
                    lowest_cell = cell
                elif cell.tries == lowest_cell.tries:
                    # Tie breaker
                    # Bigger rooms get selected first
                    if len(cell.room.cells) > len(lowest_cell.room.cells):
                        lowest_cell = cell

    return lowest_cell
