def next_forward_pruning_mrv_cell(regions, cells):
    """
    Selects next move based on minimum remaining values with some tie breaking
    between two mrv cells.
    :param regions: The regions.
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
                    # Bigger regions get selected first
                    if len(cell.region.cells) > len(lowest_cell.region.cells):
                        lowest_cell = cell

    return lowest_cell
    