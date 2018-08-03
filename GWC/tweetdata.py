import json

tweetFile = open("tweets.json", "r")

tweetData = json.load(tweetFile)

tweetFile.close()

print("Tweet id: ", tweetData[0]["id"])
print("Tweet text: ", tweetData[0]["text"])

for tweet in tweetData:
    print("Tweet text: " + tweet["text"])
