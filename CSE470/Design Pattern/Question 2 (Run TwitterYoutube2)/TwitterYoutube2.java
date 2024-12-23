public class TwitterYoutube2 {
    public static void main(String[] args) {
        Channel Twitter = new Channel("Twitter");
        Channel Youtube = new Channel("Youtube");
        Users user1 = new Users("user1");
        Users user2 = new Users("user2");
        

        System.out.println("------------------------------Twitter------------------------------");
        user1.subscribe(Twitter);
        user2.subscribe(Twitter);
        user2.subscribe(Youtube);

        Twitter.uploadVideo("Video1");
        Twitter.uploadReels("Reels 2");
        user1.unsubscribe(Twitter);
        Twitter.uploadVideo("Video 3");



    }
}
