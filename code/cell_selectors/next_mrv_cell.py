def next_mrv_cell(regions, cells):
    """
    Selects next move based on minimum remaining values.
    :param regions: The regions sorted in descending order of size.
    :param cells: The cells.
    :return: The next cell.
    """
    for idx in range(len(regions) - 1, -1, -1):
        for cell in regions[idx].cells:
            if cell.value is not None:
                continue
            return cell