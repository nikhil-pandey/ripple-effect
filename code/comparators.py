def next_empty_cell(cells):
    for row in cells:
        for cell in row:
            if not cell.has_value():
                return cell


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


def next_human_line_mrv_cell(cells):
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

def default_next_move(cell):
    return cell.get_moves()