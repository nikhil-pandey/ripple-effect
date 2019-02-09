import java.util.List;
import java.util.Map;


public interface Pruner {
    boolean isSuccessful();

    List< Map< Cell, Integer > > prune( Grid grid, Cell cell );
}
