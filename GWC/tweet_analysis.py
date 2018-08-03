import json
from textblob import TextBlob
import matplotlib.pyplot as plt
#from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below!  

# Textblob
polarity = []
subjectivity = []
all_tweets = " "

for tweet in tweetData:
    x = (tweet["text"])
    all_tweets += x
#print(all_tweets)



##for tweet in tweetData:
##    tb = TextBlob(tweet["text"])
##    x = tb.polarity
##    polarity.append(x)
##    polSum = sum(polarity)
##    polLen = len(polarity)
##    polAvg = polSum/polLen
##
##for tweet in tweetData:
##    tb = TextBlob(tweet["text"])
##    x = tb.subjectivity
##    subjectivity.append(x)
##    subSum = sum(subjectivity)
##    subLen = len(subjectivity)
##    subAvg = subSum/subLen
##
##print(polAvg)
##print(subAvg)
##
##plt.hist(polarity, histtype = 'bar')
##plt.ylabel('Frequency')
##plt.hist(subjectivity, histtype = 'bar')
##plt.ylabel('Frequency')
##plt.show()   
##                   
    
