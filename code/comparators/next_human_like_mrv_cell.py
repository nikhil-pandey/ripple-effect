import logging


def next_human_like_mrv_cell(rooms, cells):
    """
    Human like decision with fallback to MRV.
    Deduces cells that have no other possible options and prioritizes them.
    Else falls back to minimum remaining values.
    :param rooms: The rooms.
    :param cells: The cells.
    :return: The next cell.
    """
    lowest_count = 0
    lowest_cell = None

    for room in rooms:
        for number, cells in room.get_options().items():
            if len(cells) == 1:
                for cell in cells:
                    if cell.has_value():
                        continue
                    # logging.debug('COMPARATOR: Only valid value: %s for
                    # cell: %s' % (number, cell))
                    cell.assign_next_move(number)
                    return cell

        for cell in room.get_cells():
            if cell.has_value():
                continue

            if lowest_cell is None or cell.get_move_count() < lowest_count:
                lowest_count = cell.get_move_count()
                lowest_cell = cell
            elif cell.get_move_count() == lowest_count:
                # Tie breaker
                # Most tried cells are prioritized first
                if cell.get_tries() > lowest_cell.get_tries():
                    lowest_cell = cell
                elif cell.get_tries() == lowest_cell.get_tries():
                    # Tie breaker
                    # Bigger rooms get selected first
                    if cell.get_room().get_size() > lowest_cell.get_room().get_size():
                        lowest_cell = cell

    # logging.debug('COMPARATOR: Lowest number of moves: %d found for Cell:
    # %s' % (lowest_count, lowest_cell))
    return lowest_cell
