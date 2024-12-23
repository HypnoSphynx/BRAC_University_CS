public class TwitchAdapter implements wechatAdapter{ 

    private final Twitch twitch; 

    public TwitchAdapter() {
        this.twitch = new Twitch();
    }

    @Override
    public void getStream() {
        twitch.streamVideo();
    }
    @Override
    public void setSendingMessage() {
    }

    @Override
    public void getNewsFeed() {

    }

    @Override
    public void setCreateGroups() {

    }
       
    
}
