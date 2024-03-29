from cell import Cell
from region import Region
from .base_reader import BaseReader
from collections import deque
from pruners import forward_pruner


class GridReader(BaseReader):

    def __init__(self, file_name):
        """
        Sets up the grid.
        :param file_name: Name of the file or String like input.
        """
        super().__init__(file_name)
        self.regions = []
        self.__prepare()

    def __prepare(self):
        """
        Prepares the grid by doing a dfs search to figure out the regions.
        :return: None
        """
        main_visited = set()
        for i in range(0, self.cell_count):
            row = i // self.column_count
            col = i - row * self.column_count

            if (row, col) in main_visited:
                continue

            region = Region()
            self.regions.append(region)
            cell = self.__get_or_create_cell(region, row, col)

            visited = set()
            main_visited.add((row, col))
            visited.add((row, col))

            region_queue = deque()
            region_queue.append((cell.row, cell.col))

            while region_queue:

                state = region_queue.popleft()
                successors = self.__get_successors(state)

                for row, col in successors:
                    if (row, col) not in visited:
                        self.__get_or_create_cell(region, row, col)
                        main_visited.add((row, col))
                        visited.add((row, col))
                        region_queue.append((row, col))

        self.regions.sort(key=lambda x: len(x.cells), reverse=True)
        cell_having_values = []
        for region in self.regions:
            for number in range(1, len(region.cells) + 1):
                for cell in region.cells:
                    if cell.value is not None:
                        cell_having_values.append(cell)
                        continue
                    cell.possible_moves.add(number)
                    if number not in region.possible_options:
                        region.possible_options[number] = set()
                    region.possible_options[number].add(cell)

        # Remove possible values from around cells that already have values
        for cell in cell_having_values:
            forward_pruner(self, cell)

    def __get_successors(self, position):
        """
        Get successors of a position
        :param position: tuple of row, col
        :return: Generates the successors
        """
        actual_grid_pos = position[0] * 2 + 1, position[1] * 2 + 1

        sfs = [
            lambda x, y: ((x + 1, y), ((x + 2) // 2, y // 2)),
            lambda x, y: ((x - 1, y), ((x - 2) // 2, y // 2)),
            lambda x, y: ((x, y + 1), (x // 2, (y + 2) // 2)),
            lambda x, y: ((x, y - 1), (x // 2, (y - 2) // 2)),
        ]

        for s in sfs:
            separator, actual_succ_posn = s(*actual_grid_pos)

            if actual_succ_posn[0] < 0 or actual_succ_posn[0] - 1 >= \
                    self.row_count \
                    or actual_succ_posn[1] < 0 or actual_succ_posn[
                1] - 1 >= self.column_count:
                continue

            if self.input_grid[separator[0]][separator[1]] == '|' or \
                    self.input_grid[separator[0]][separator[1]] == '-':
                continue

            yield actual_succ_posn

    def __get_or_create_cell(self, region, row, col):
        """
        Returns the cell if it already exists else creates a new cell.
        :param region: The region cell is in.
        :param row: The row.
        :param col: The col.
        :return: The cell.
        """
        if not self.cells[row][col]:
            value = self.input_grid[row * 2 + 1][col * 2 + 1]
            value = int(value) if value != '.' else None
            self.cells[row][col] = Cell(row, col, value)
            self.cells[row][col].region = region
            region.cells.add(self.cells[row][col])

        return self.cells[row][col]
