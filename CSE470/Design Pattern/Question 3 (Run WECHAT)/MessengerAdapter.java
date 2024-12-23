public class MessengerAdapter implements wechatAdapter{

    private final Messenger messenger;


    public MessengerAdapter() {
        this.messenger = new Messenger();
    }

    @Override
    public void setSendingMessage() {
        messenger.sendMessage();
    }

    @Override
    public void getStream() {
    }

    @Override
    public void getNewsFeed() {
    }

    @Override
    public void setCreateGroups() {
    }

}


