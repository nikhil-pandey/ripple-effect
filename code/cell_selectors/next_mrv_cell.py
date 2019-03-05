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

    return lowest_cell