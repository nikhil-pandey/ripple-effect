def next_empty_cell(regions, cells):
    """
    Returns the next empty cell in the grid.
    :param regions: The regions.
    :param cells: The cells.
    :return: The next cell to try to fill.
    """
    for row in cells:
        for cell in row:
            if cell.value is None:
                return cell