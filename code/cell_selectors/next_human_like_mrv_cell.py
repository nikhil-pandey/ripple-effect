def next_human_like_mrv_cell(regions, cells):
    """
    Human like decision with fallback to MRV.
    Deduces cells that have no other possible options and prioritizes them.
    Else falls back to minimum remaining values.
    :param regions: The regions.
    :param cells: The cells.
    :return: The next cell.
    """
    lowest_count = 0
    lowest_cell = None

    for region in regions:
        for number, cells in region.possible_options.items():
            if len(cells) == 1:
                for cell in cells:
                    if cell.value is not None:
                        continue
                    cell.next_move = number
                    return cell

        for cell in region.cells:
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
