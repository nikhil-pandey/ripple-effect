import logging


def next_empty_cell(rooms, cells):
    # logging.debug('COMPARATOR: Finding next empty cell')
    for row in cells:
        for cell in row:
            if not cell.has_value():
                # logging.debug('COMPARATOR: Found next cell: %s' % (cell))
                return cell
