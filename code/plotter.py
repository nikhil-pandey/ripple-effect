import matplotlib.pyplot as plt
from matplotlib import animation


class Plotter(object):
    def __init__(self, grid, moves=[], cell_size=1, out_file=None):
        self.grid = grid
        self.cell_size = cell_size
        self.height = grid.row_count * cell_size
        self.width = grid.column_count * cell_size
        self.ax = None
        self.texts = {}
        self.moves = moves
        self.out_file = out_file

    def show_solution(self):
        self.configure_plot()
        self.__make_grid(self.grid.cells)
        plt.show()

    def __make_grid(self, cells):
        row_count = len(cells)
        for i, row in enumerate(cells):
            for j, cell in enumerate(row):
                actual_grid_pos = i * 2 + 1, j * 2 + 1

                plot_i = row_count - i

                if cell.value is not None:
                    self.texts[i * row_count + j] = \
                        self.ax.text((2 * j + 0.7) * self.cell_size / 2,
                                     (2 * plot_i + 0.7) * self.cell_size / 2,
                                     cell.value, fontsize=10,
                                     weight='bold')

                if self.grid.input_grid[actual_grid_pos[0] - 1][
                    actual_grid_pos[1]] != ' ':
                    self.ax.plot(
                        [(j + 1) * self.cell_size, j * self.cell_size],
                        [(plot_i + 1) * self.cell_size,
                         (plot_i + 1) * self.cell_size], color='k')
                else:
                    if self.grid.input_grid[actual_grid_pos[0] - 1][
                        actual_grid_pos[1]] != ' ':
                        self.ax.plot(
                            [(j + 1) * self.cell_size, j * self.cell_size],
                            [(plot_i + 1) * self.cell_size,
                             (plot_i + 1) * self.cell_size], color='k',
                            linestyle=':')
                if self.grid.input_grid[actual_grid_pos[0]][
                    actual_grid_pos[1] + 1] != ' ':
                    self.ax.plot(
                        [(j + 1) * self.cell_size, (j + 1) * self.cell_size],
                        [plot_i * self.cell_size,
                         (plot_i + 1) * self.cell_size], color='k')
                else:
                    self.ax.plot(
                        [(j + 1) * self.cell_size, (j + 1) * self.cell_size],
                        [plot_i * self.cell_size,
                         (plot_i + 1) * self.cell_size], color='k',
                        linestyle=':')

                if self.grid.input_grid[actual_grid_pos[0] + 1][
                    actual_grid_pos[1]] != ' ':
                    self.ax.plot(
                        [j * self.cell_size, (j + 1) * self.cell_size],
                        [plot_i * self.cell_size, plot_i * self.cell_size],
                        color='k')
                else:
                    self.ax.plot(
                        [j * self.cell_size, (j + 1) * self.cell_size],
                        [plot_i * self.cell_size, plot_i * self.cell_size],
                        color='k', linestyle=':')

                if self.grid.input_grid[actual_grid_pos[0]][
                    actual_grid_pos[1] - 1] != ' ':
                    self.ax.plot([j * self.cell_size, j * self.cell_size],
                                 [(plot_i + 1) * self.cell_size,
                                  plot_i * self.cell_size], color='k')
                else:
                    self.ax.plot([j * self.cell_size, j * self.cell_size],
                                 [(plot_i + 1) * self.cell_size,
                                  plot_i * self.cell_size], color='k',
                                 linestyle=':')

    def configure_plot(self):
        fig = plt.figure(figsize=(
            7, 7 * self.grid.row_count / self.grid.column_count))

        self.ax = plt.axes()
        self.ax.set_aspect("equal")

        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.axes.get_yaxis().set_visible(False)

        self.ax.text(0, self.grid.row_count + self.cell_size + 0.1,
                     r'%s$\times$%s' % (
                         self.grid.row_count,
                         self.grid.column_count),
                     bbox={'facecolor': 'gray', 'alpha': 0.5, 'pad': 4},
                     fontname='serif',
                     fontsize=15)
        return fig

    def animate(self):
        fig = self.configure_plot()
        self.__make_grid(self.grid.cells)
        actions = ('Solve Called', 'Move Selected', 'Validation Failed', 'Assigned Move', 'Wrong Move')

        def make_frame(frame):
            action, row, col, val = self.moves[frame]
            position = self.grid.column_count * row + col
            if action == 3:
                if position in self.texts:
                    self.texts[position].set_visible(True)
                    self.texts[position].set_text(val)
                else:
                    self.texts[position] = self.ax.text(
                        (2 * col + 0.7) * self.cell_size / 2, (
                                2 * (
                                self.grid.row_count - row) + 0.7) *
                        self.cell_size
                        / 2,
                        val, fontsize=10, weight='bold')
            elif action == -1:
                if position in self.texts:
                    self.texts[position].set_visible(False)
            nonlocal actions
            self.ax.set_title(
                'Row: %d Col: %d Val: %d\n%s' % (row, col, val, actions[action]),
                fontname='serif', fontsize=17)
            return []

        anim = animation.FuncAnimation(fig, make_frame,
                                       frames=self.moves.__len__(),
                                       interval=10, blit=True, repeat=False)
        if self.out_file is not None:
            anim.save(self.out_file, fps=1)
        plt.show()