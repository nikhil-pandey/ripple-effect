import java.util.List;
import java.util.Map;


public class DefaultPruner implements Pruner {
    @Override
    public List< Map< Cell, Integer > > prune( Grid grid, Cell cell ) {
        return null;
    }

    @Override public boolean isSuccessful() {
        return false;
    }
}
