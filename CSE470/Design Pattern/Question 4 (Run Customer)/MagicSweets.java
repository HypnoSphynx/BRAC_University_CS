public class MagicSweets {

    private static MagicSweets cake;

    public static MagicSweets bakeCake() {
        if (cake == null) {
            cake = new MagicSweets();
        }
        return cake;

    }

    
    
}
