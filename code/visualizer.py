import matplotlib.pyplot as plt
from matplotlib import animation
import logging

from readers import GridReader

logging.basicConfig(level=logging.DEBUG)


class Visualizer(object):
    """Class that handles all aspects of visualization.


    Attributes:
        grid: The grid that will be visualized
        cell_size (int): How large the cells will be in the plots
        height (int): The height of the grid
        width (int): The width of the grid
        ax: The axes for the plot
        lines:
        squares:
        media_filename (string): The name of the animations and images

    """
    def __init__(self, grid, cell_size, media_filename, all_grids):
        self.grid = grid
        self.cell_size = cell_size
        self.height = grid.get_row_count() * cell_size
        self.width = grid.get_column_count() * cell_size
        self.ax = None
        self.lines = dict()
        self.squares = dict()
        self.media_filename = media_filename
        self.path = all_grids

    def set_media_filename(self, filename):
        """Sets the filename of the media
            Args:
                filename (string): The name of the media
        """
        self.media_filename = filename

    def show_grid(self):
        """Displays a plot of the grid without the solution path"""

        # Create the plot figure and style the axes
        fig = self.configure_plot()

        # Plot the walls on the figure
        self.plot(self.grid.get_cells())

        # Display the plot to the user
        plt.show()

        # Handle any potential saving
        if self.media_filename:
            fig.savefig("{}{}.png".format(self.media_filename, "_generation"), frameon=None)

    def plot(self, cells):
        """ Plots the rooms of a grid. This is used when generating the grid image"""
        for txt in self.ax.texts:
            txt.set_visible(False)

        row_count = len(cells)
        for i, row in enumerate(cells):
            for j, cell in enumerate(row):
                actual_grid_pos = i * 2 + 1, j * 2 + 1

                plot_i = row_count - i

                if cell.has_value():
                    self.ax.text((2*j + 0.7)*self.cell_size/2, (2*plot_i + 0.7)*self.cell_size/2, cell.get_value(), fontsize=10, weight='bold')

                if self.grid._input_grid[actual_grid_pos[0]-1][actual_grid_pos[1]] != ' ':
                    self.ax.plot([(j + 1) * self.cell_size, j * self.cell_size],
                                 [(plot_i + 1) * self.cell_size, (plot_i + 1) * self.cell_size], color="k")

                if self.grid._input_grid[actual_grid_pos[0]][actual_grid_pos[1]+1] != ' ':
                    self.ax.plot([(j+1)*self.cell_size, (j+1)*self.cell_size],
                                 [plot_i*self.cell_size, (plot_i+1)*self.cell_size], color="k")

                if self.grid._input_grid[actual_grid_pos[0]+1][actual_grid_pos[1]] != ' ':
                    self.ax.plot([j*self.cell_size, (j+1)*self.cell_size],
                                 [plot_i*self.cell_size, plot_i*self.cell_size], color="k")

                if self.grid._input_grid[actual_grid_pos[0]][actual_grid_pos[1]-1] != ' ':
                    self.ax.plot([j*self.cell_size, j*self.cell_size],
                                 [(plot_i+1)*self.cell_size, plot_i*self.cell_size], color="k")

    def configure_plot(self):
        """Sets the initial properties of the grid plot. Also creates the plot and axes"""

        # Create the plot figure
        fig = plt.figure(figsize = (7, 7*self.grid.get_row_count()/self.grid.get_column_count()))

        # Create the axes
        self.ax = plt.axes()

        # Set an equal aspect ratio
        self.ax.set_aspect("equal")

        # Remove the axes from the figure
        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.axes.get_yaxis().set_visible(False)

        title_box = self.ax.text(0, self.grid.get_row_count() + self.cell_size + 0.1,
                            r"{}$\times${}".format(self.grid.get_row_count(), self.grid.get_column_count()),
                            bbox={"facecolor": "gray", "alpha": 0.5, "pad": 4}, fontname="serif", fontsize=15)

        return fig

    def show_grid_solution(self):
        """Function that plots the solution to the grid. Also adds indication of entry and exit points."""

        # Create the figure and style the axes
        fig = self.configure_plot()

        # Plot the walls onto the figure
        self.plot(self.grid.get_cells())

        # Display the plot to the user
        plt.show()

        # Handle any saving
        if self.media_filename:
            fig.savefig("{}{}.png".format(self.media_filename, "_solution"), frameon=None)

    def animate_grid_solution(self):
        """Function that animates the process of generating the a grid where path is a list
        of coordinates indicating the path taken to carve out (break down walls) the grid."""

        # Create the figure and style the axes
        fig = self.configure_plot()

        self.plot(GridReader(self.path[0]).get_cells())

        def animate(frame):
            print(frame, len(self.path))
            self.plot(GridReader(self.path[frame]).get_cells())
            self.ax.set_title("Step: {}".format(frame + 1), fontname = "serif", fontsize = 19)
            return []

        logging.debug("Creating solution animation")
        anim = animation.FuncAnimation(fig, animate, frames=self.path.__len__(),
                                       interval=100, blit=True, repeat=False)
        logging.debug("Finished creating solution animation")

        # Display the animation to the user
        plt.show()

        # Handle any saving
        if self.media_filename:
            print("Saving solution animation. This may take a minute....")
            mpeg_writer = animation.FFMpegWriter(fps=24, bitrate=1000)
            anim.save("{}{}{}x{}.mp4".format(self.media_filename, "_solution_", self.grid.get_row_count(),
                                           self.grid.get_column_count()), writer=mpeg_writer)