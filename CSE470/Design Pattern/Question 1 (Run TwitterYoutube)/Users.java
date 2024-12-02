public class Users {
    private final String name;
    
    public Users(String name) {
        super();
        this.name = name;
        System.out.println("User created: " + name);
    }

    public String getName() {
        return this.name;
    }


    public void subscribe(Channel channel) {
       channel.add(this);
    }

    public void unsubscribe(Channel channel) {
        channel.remove(this);
    }

}
