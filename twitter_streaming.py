#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = 991128944-4iBCV66Z9phPWx6PU5NVpnHnLhFmDw5qv95cYHZ7
access_token_secret = HYicyauShZw1KSEHIAKd3K7jqNZcnvoFYduvNzCUmtQdA
consumer_key = 3CPUFhgxy4wt5BoIxT4r52Rcm
consumer_secret = VzhCemVlAmdJbhrFIPBU0yDIDorPl2jFfqFvhOo08s0sjHwvtE


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

   
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'Almaty', 'good', 'bad', 
    stream.filter(track=['Almaty', 'good', 'bad'])
