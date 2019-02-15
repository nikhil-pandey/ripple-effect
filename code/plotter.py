import matplotlib.pyplot as plt
from matplotlib import animation


class Plotter(object):
    def __init__(self, grid, cell_size, moves):
        self.grid = grid
        self.cell_size = cell_size
        self.height = grid.get_row_count() * cell_size
        self.width = grid.get_column_count() * cell_size
        self.ax = None
        self.texts = {}
        self.moves = moves

    def show_grid(self):
        fig = self.configure_plot()
        self.make_grid(self.grid.get_cells())
        plt.show()

    def make_grid(self, cells):
        row_count = len(cells)
        for i, row in enumerate(cells):
            for j, cell in enumerate(row):
                actual_grid_pos = i * 2 + 1, j * 2 + 1

                plot_i = row_count - i

                if cell.has_value():
                    self.texts[i * row_count + j] = \
                        self.ax.text((2 * j + 0.7) * self.cell_size / 2, (2 * plot_i + 0.7) * self.cell_size / 2,
                                     cell.get_value(), fontsize=10, weight='bold')

                if self.grid._input_grid[actual_grid_pos[0] - 1][actual_grid_pos[1]] != ' ':
                    self.ax.plot([(j + 1) * self.cell_size, j * self.cell_size],
                                 [(plot_i + 1) * self.cell_size, (plot_i + 1) * self.cell_size], color='k')
                else:
                    if self.grid._input_grid[actual_grid_pos[0] - 1][actual_grid_pos[1]] != ' ':
                        self.ax.plot([(j + 1) * self.cell_size, j * self.cell_size],
                                     [(plot_i + 1) * self.cell_size, (plot_i + 1) * self.cell_size], color='k', linestyle=':')
                if self.grid._input_grid[actual_grid_pos[0]][actual_grid_pos[1] + 1] != ' ':
                    self.ax.plot([(j + 1) * self.cell_size, (j + 1) * self.cell_size],
                                 [plot_i * self.cell_size, (plot_i + 1) * self.cell_size], color='k')
                else:
                    self.ax.plot([(j + 1) * self.cell_size, (j + 1) * self.cell_size],
                                 [plot_i * self.cell_size, (plot_i + 1) * self.cell_size], color='k', linestyle=':')

                if self.grid._input_grid[actual_grid_pos[0] + 1][actual_grid_pos[1]] != ' ':
                    self.ax.plot([j * self.cell_size, (j + 1) * self.cell_size],
                                 [plot_i * self.cell_size, plot_i * self.cell_size], color='k')
                else:
                    self.ax.plot([j * self.cell_size, (j + 1) * self.cell_size],
                                 [plot_i * self.cell_size, plot_i * self.cell_size], color='k', linestyle=':')

                if self.grid._input_grid[actual_grid_pos[0]][actual_grid_pos[1] - 1] != ' ':
                    self.ax.plot([j * self.cell_size, j * self.cell_size],
                                 [(plot_i + 1) * self.cell_size, plot_i * self.cell_size], color='k')
                else:
                    self.ax.plot([j * self.cell_size, j * self.cell_size],
                                 [(plot_i + 1) * self.cell_size, plot_i * self.cell_size], color='k', linestyle=':')

    def configure_plot(self):
        fig = plt.figure(figsize=(7, 7 * self.grid.get_row_count() / self.grid.get_column_count()))

        self.ax = plt.axes()
        self.ax.set_aspect("equal")

        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.axes.get_yaxis().set_visible(False)

        title_box = self.ax.text(0, self.grid.get_row_count() + self.cell_size + 0.1,
                                 r"{}$\times${}".format(self.grid.get_row_count(), self.grid.get_column_count()),
                                 bbox={"facecolor": "gray", "alpha": 0.5, "pad": 4}, fontname="serif", fontsize=15)
        return fig

    def animate(self):
        fig = self.configure_plot()

        self.make_grid(self.grid.get_cells())

        counter = 0

        def make_frame(frame):
            # for x in range(frame * 10, min(len(self.moves), frame*10 + 10)):
            x = frame
            action, row, col, val = self.moves[x]
            nonlocal counter
            position = self.grid.get_column_count() * row + col
            if action == 0:
                counter += 1
            elif action == 1:
                if position in self.texts:
                    self.texts[position].set_visible(True)
                    self.texts[position].set_text(val)
                else:
                    self.texts[position] = self.ax.text((2 * col + 0.7) * self.cell_size / 2, (
                                2 * (self.grid.get_row_count() - row) + 0.7) * self.cell_size / 2,
                                                        val, fontsize=10, weight='bold')
            elif action == -1:
                if position in self.texts:
                    self.texts[position].set_visible(False)

            self.ax.set_title("Step: {} , {}".format(counter, str((action, row, col, val))), fontname="serif", fontsize=19)
            return []

        anim = animation.FuncAnimation(fig, make_frame, frames=self.moves.__len__(), # // 10 + 1,
                                       interval=10, blit=True, repeat=False)
        anim.save('final.mp4', fps=10)
        plt.show()
