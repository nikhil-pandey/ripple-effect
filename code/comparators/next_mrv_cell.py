def next_mrv_cell(cells):
    lowest_count = 0
    lowest_cell = None
    for row in cells:
        for cell in row:
            if (not cell.has_value()) and \
                    (lowest_cell is None or
                     cell.get_move_count() < lowest_count):
                lowest_count = cell.get_move_count()
                lowest_cell = cell
    return lowest_cell
