def next_human_line_mrv_cell(cells):
    # TODO: human like feature
    lowest_count = 0
    lowest_cell = None
    for row in cells:
        for cell in row:
            if (not cell.has_value()) and \
                    (lowest_cell is None or
                     len(cell.possible_moves) < lowest_count):
                lowest_count = cell.get_move_count()
                lowest_cell = cell
    return lowest_cell