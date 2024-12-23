import java.util.ArrayList;
import java.util.List;

public class Users {
    private String name;
    private List<Channel> Channels = new ArrayList<>();
    

    public Users(String name) {
        super();
        this.name = name;
        System.out.println("User created: " + name);

    }


    public void subscribe(Channel ch) {
        if (Channels.contains(ch)) {
            System.out.println(name + " already subscribed to " + ch.title);
            return;
        }
        Channels.add(ch);
        ch.adding(this);
        System.out.println(name + " subscribed to " + ch.title);
    }

    public void unsubscribe(Channel ch) {
        if (!Channels.contains(ch)) {
            System.out.println(name + " not subscribed to " + ch.title);
            return;
        }
        Channels.remove(ch);
        ch.removing(this);
        
    }

    public String getName() {
        return this.name;
    }
    
    public void notify(String video, Channel ch, int i) {
        if (i == 0) {
            System.out.println("Hey " + this.name + " Video Uploaded : " + video + " from " + ch.title);
        } else
        if (Channels.contains(ch)) {
            System.out.println("Hey " + this.name + " Reels Uploaded : " + video + " from " + ch.title);
        }
    }

}