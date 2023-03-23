word_dict = {
    # Positive words
    "love": 1,
    "happy": 1,
    "excited": 1,
    "kind": 1,
    "amazing": 1,
    "fantastic": 1,
    "awesome": 1,
    "good": 1,
    "delightful": 1,
    "excellent": 1,
    "beautiful": 1,
    "wonderful": 1,
    "pleasure": 1,
    "enjoy": 1,
    "satisfy": 1,
    "pleased": 1,
    "fun": 1,
    "jolly": 1,
    "smile": 1,
    "cheer": 1,
    
    # Neutral words
    "the": 0,
    "it": 0,
    "and": 0,
    "is": 0,
    "that": 0,
    "of": 0,
    "in": 0,
    "to": 0,
    "with": 0,
    "for": 0,
    "on": 0,
    "at": 0,
    "by": 0,
    "about": 0,
    "as": 0,
    "this": 0,
    "be": 0,
    "but": 0,
    "from": 0,
    
    # Negative words
    "hate": -1,
    "sad": -1,
    "angry": -1,
    "bad": -1,
    "unhappy": -1,
    "disappointed": -1,
    "terrible": -1,
    "annoyed": -1,
    "frustrated": -1,
    "upset": -1,
    "worry": -1,
    "regret": -1,
    "dislike": -1,
    "miss": -1,
    "hurt": -1,
    "pain": -1,
    "grieve": -1,
    "cry": -1,
    "fear": -1,
    "stress": -1
}
def classify_tweet(tweet):
    # Split tweet into individual words
    words = tweet.lower().split()
    
    # Calculate sentiment score for tweet
    score = 0
    for word in words:
        if word in word_dict:
            score += word_dict[word]
    
    # Classify tweet based on sentiment score
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"

# Example tweets
tweet1 = "I love spending time with my family"
tweet2 = "This traffic is making me so angry"
tweet3 = "The weather today is nice"

# Classify tweets
print(classify_tweet(tweet1)) 
print(classify_tweet(tweet2))
print(classify_tweet(tweet3))
