public class FacebookAdapter implements wechatAdapter {
    private final Faceook facebook;

    
    public FacebookAdapter() {
        this.facebook = new Faceook();
    }

    @Override
    public void getNewsFeed() {
        facebook.newsFeed();
    }

    @Override
    public void setCreateGroups() {
        facebook.createGroups();
    }
    
    @Override
    public void setSendingMessage() {
    }

    @Override
    public void getStream() {
    }




}