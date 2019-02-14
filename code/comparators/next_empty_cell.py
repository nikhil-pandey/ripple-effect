def next_empty_cell(cells):
    for row in cells:
        for cell in row:
            if not cell.has_value():
                return cell
