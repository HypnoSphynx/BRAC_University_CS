public class WECHAT {
    private static WECHAT instance;


    
    public static WECHAT getInstance() {
        if (instance == null) {
            instance = new WECHAT();
        }
        return instance;
    }

    wechatAdapter facebookAdapter;
    wechatAdapter messengerAdapter;
    wechatAdapter twitchAdapter;

    
    public wechatAdapter getFacebookAdapter() {
        return facebookAdapter;
    }

    public wechatAdapter getMessengerAdapter() {
        return messengerAdapter;
    }

    public wechatAdapter getTwitchAdapter() {
        return twitchAdapter;
    }
    
    public void setFacebookAdapter(wechatAdapter facebookAdapter) {
        this.facebookAdapter = facebookAdapter;
    }

    public void setMessengerAdapter(wechatAdapter messengerAdapter) {
        this.messengerAdapter = messengerAdapter;
    }

    public void setTwitchAdapter(wechatAdapter twitchAdapter) {
        this.twitchAdapter = twitchAdapter;
    }

    public void sendMessage() {
        messengerAdapter.setSendingMessage();
    }

    public void streamingVideo() {
        twitchAdapter.getStream();
    }

    public void useNewsFeed() {
        facebookAdapter.getNewsFeed();
    }

    public void createFriendsGroup() {
        facebookAdapter.setCreateGroups();
    }

    
    public static void main(String[] args) {
        WECHAT weChat = WECHAT.getInstance();
        FacebookAdapter facebookAdapter = new FacebookAdapter();
        MessengerAdapter messengerAdapter = new MessengerAdapter();
        TwitchAdapter twitchAdapter = new TwitchAdapter();
        weChat.setFacebookAdapter(facebookAdapter);
        weChat.setMessengerAdapter(messengerAdapter);
        weChat.setTwitchAdapter(twitchAdapter);
        weChat.streamingVideo();
        WECHAT weChat2 = WECHAT.getInstance();
        weChat.sendMessage();
        weChat.createFriendsGroup();
        weChat2.useNewsFeed();
        System.out.println(weChat);
        System.out.println(weChat2);

        
    }





}
