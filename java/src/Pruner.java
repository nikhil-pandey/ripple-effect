import java.util.List;
import java.util.Map;


public interface Pruner {
    List< Map<Cell, Integer>> prune( Grid grid, Cell cell );

    boolean isSuccessful();
}
