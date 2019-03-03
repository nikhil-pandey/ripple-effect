def default_pruner(grid, cell):
    """
    Default pruner. Doesn't do anything.
    :param grid: The grid.
    :param cell: The cell that was changed.
    :return: Tuple of removed values and if the search should continue
    """
    return [], True
