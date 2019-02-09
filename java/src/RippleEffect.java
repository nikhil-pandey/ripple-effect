public class RippleEffect {
    public static void main( String[] args ) {
        String fileName = "test";

        Grid grid = new Grid( new Reader( fileName ) );

        Solver bruteForceSolver =
                new Solver( new SimpleValidator(), new FirstEmptySelector(),
                        new DefaultCellSorter(), new DefaultValueSorter(),
                        new DefaultPruner() );

        bruteForceSolver.solve( grid );
    }
}
