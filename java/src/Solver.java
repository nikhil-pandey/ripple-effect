import java.util.List;
import java.util.Map;


public class Solver {

    /**
     * The validator
     */
    private final Validator validator;

    /**
     * Next Variable Selector
     */
    private final CellSelector cellSelector;

    private final CellSorter cellSorter;
    private final ValueSorter valueSorter;
    private final Pruner pruner;

    public Solver( Validator validator, CellSelector cellSelector,
                   CellSorter cellSorter, ValueSorter valueSorter,
                   Pruner pruner ) {
        this.validator = validator;
        this.cellSelector = cellSelector;
        this.cellSorter = cellSorter;
        this.valueSorter = valueSorter;
        this.pruner = pruner;
    }

    public Grid solve( Grid grid ) {
        Cell cell = this.cellSelector.next( grid, this.cellSorter );

        if ( cell == null ) {
            return grid;
        }

        for ( int value : this.valueSorter.sort( cell ) ) {
            if ( !this.validator.isValid( grid, cell, value ) ) {
                continue;
            }

            grid.assign( cell, value );

            List< Map< Cell, Integer > > pruned =
                    this.pruner.prune( grid, cell );

            if ( this.pruner.isSuccessful() ) {
                Grid solution = this.solve( grid );

                if ( solution != null ) {
                    return solution;
                }
            }

            grid.rollback( cell, pruned );
        }

        return null;
    }
}
