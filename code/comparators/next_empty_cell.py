import logging


def next_empty_cell(rooms, cells):
    """
    Returns the next empty cell in the grid.
    :param rooms: The rooms.
    :param cells: The cells.
    :return: The next cell to try to fill.
    """
    # logging.debug('COMPARATOR: Finding next empty cell')
    for row in cells:
        for cell in row:
            if not cell.has_value():
                # logging.debug('COMPARATOR: Found next cell: %s' % (cell))
                return cell
