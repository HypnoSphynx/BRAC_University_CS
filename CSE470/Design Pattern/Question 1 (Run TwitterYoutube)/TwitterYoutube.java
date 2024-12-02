public class TwitterYoutube {
    public static void main(String[] args) {
        
        Users user1 = new Users("Zawad");
        Users user2 = new Users("Nahid");
        Users user3 = new Users("Rial");

        Channel channel = Channel.getInstance();
        Channel channel2 = Channel.getInstance();
        user1.subscribe(channel);
        user2.subscribe(channel);
        user3.subscribe(channel);

        channel.uploadVideo("This is video 01");
        channel.uploadVideo("This is video 02");
        channel2.uploadVideo("This is video 03");

        user1.unsubscribe(channel);
        user2.unsubscribe(channel);

        channel.uploadVideo("This is video 04");
        

    }
}
