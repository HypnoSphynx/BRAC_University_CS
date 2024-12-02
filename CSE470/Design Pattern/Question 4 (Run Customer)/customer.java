public class customer {
    public static void main(String[] args) {
        MagicSweets cake = MagicSweets.bakeCake();
        System.out.println(cake);
        MagicSweets cake2 = MagicSweets.bakeCake();
        System.out.println(cake2);
    }
}
