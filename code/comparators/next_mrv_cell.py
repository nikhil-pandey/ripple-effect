import logging


def next_mrv_cell(rooms, cells):
    # logging.debug('COMPARATOR: Finding next MRV Cell')
    lowest_count = 0
    lowest_cell = None
    for row in cells:
        for cell in row:
            if cell.has_value():
                continue
            if lowest_cell is None or cell.get_move_count() < lowest_count:
                lowest_count = cell.get_move_count()
                lowest_cell = cell
            elif cell.get_move_count() == lowest_count:
                if cell.get_tries() > lowest_cell.get_tries():
                    lowest_cell = cell
                elif cell.get_tries() == lowest_cell.get_tries():
                    if cell.get_room().get_size() > lowest_cell.get_room().get_size():
                        lowest_cell = cell

    # logging.debug('COMPARATOR: Lowest number of moves: %d found for Cell: %s' % (lowest_count, lowest_cell))
    return lowest_cell
