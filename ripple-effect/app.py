from flask import Flask, request, jsonify, make_response
from solvers import *
from readers import *
from cell_selectors import *
from move_selectors import *
from validators import *
from pruners import *
import time

app = Flask(__name__)


@app.route('/ripple-effect', methods=['POST'])
def SolveRippleEffect():
    solvers = {
        1: next_empty_cell,
        2: next_mrv_cell,
        3: next_forward_pruning_mrv_cell,
        4: next_human_like_mrv_cell,
    }

    which_solver = solvers[int(request.form['solver'])]
    pruner = default_pruner if which_solver in [next_empty_cell, next_mrv_cell] else forward_pruner
    file_content = request.form['puzzle']

    log = []
    counter = [0, 0, 0, 0, 0]
    solver = Solver(
        which_solver,
        default_next_move,
        localized_validator,
        pruner,
        log,
        counter
    )

    grid = GridReader(file_content)

    start_time = time.time()
    solved_grid = solver.solve(grid)
    elapsed_time = time.time() - start_time

    return make_response(jsonify(
        {'solution': str(solved_grid), 'elapsed_time': elapsed_time, 'calls_to_solve': counter[0],
         'total_moves_evaluated': counter[1], 'moves_validation_failed': counter[2], 'assigned_moves': counter[3],
         'wrong_moves_assigned': counter[4]}), 200)


if __name__ == "__main__":
    app.run(port=5001)
