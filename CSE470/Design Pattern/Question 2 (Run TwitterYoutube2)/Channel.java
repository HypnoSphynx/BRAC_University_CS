import java.util.ArrayList;

public class Channel {

    public String title;
    private ArrayList<Users> subscribers = new ArrayList<>();

    public Channel(String title) {
        super();
        this.title = title;
        System.out.println("Channel created: " + title);
    }

    public void uploadVideo(String video) {
        for (Users user : subscribers) {
            user.notify(video, this,0);
        }

    }
    public void uploadReels(String video) {
        for (Users user : subscribers) {
            user.notify(video, this,1);
        }

    }

    public void adding(Users user) {
        subscribers.add(user);
        System.out.println(user.getName() + " subscribed to " + this.title);

    }

    public void removing(Users user) {
        subscribers.remove(user);
        System.out.println(user.getName()+ " unsubscribed from " + this.title);
    }

}
