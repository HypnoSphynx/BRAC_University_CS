import java.util.ArrayList;

public class Channel {
    private static Channel instance;
    private ArrayList<String> subscribers = new ArrayList<>();
    public String name="Twitter";

    public static Channel getInstance() {
        if (instance == null) {
            
            instance = new Channel();
        }
        return instance;
    }

    public void notify(String video){
        for (String subscriber : subscribers) {
            System.out.println("Hey " + subscriber + " New Video Uploaded on TwitterYouTube " + video + " from " + name);
        }
    } 

    public void uploadVideo(String video){
        notify(video);
    }

    public void add(Users user){
        if(!subscribers.contains(user.getName())){
            subscribers.add(user.getName());
            System.out.println(user.getName() + " subscribed to Twitter");

        }else{            
        System.out.println(user.getName() + " is already subscribed to Twitter");}

    }
    public void remove(Users user){

        if (subscribers.contains(user.getName())) {
            subscribers.remove(user.getName());
            System.out.println(user.getName() + " unsubscribed from Twitter");

        } else{
        System.out.println(user.getName() + " is not subscribed to Twitter");}

    }


}
