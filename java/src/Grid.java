import java.util.List;
import java.util.Map;


public class Grid {
    private Reader reader;

    public Grid( Reader reader ) {
        this.reader = reader;
    }

    public void assign( Cell cell, int value ) {

    }

    public void rollback( Cell cell, List< Map< Cell, Integer > > pruned ) {

    }
}
