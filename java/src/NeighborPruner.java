import java.util.List;
import java.util.Map;


public class NeighborPruner implements Pruner {
    @Override public boolean isSuccessful() {
        return false;
    }

    @Override
    public List< Map< Cell, Integer > > prune( Grid grid, Cell cell ) {
        return null;
    }
}
