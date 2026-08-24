class Twitter:

    def __init__(self):
        self.tweets_by_user = {} #{user: [(counter, tweet)]}
        self.following_by_user = {} #{user: {following set()}}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # attach counter to each tweets - to track the latest tweets.
        self.count += 1

        if userId in self.tweets_by_user:
            self.tweets_by_user[userId].append((self.count, tweetId))
        else:
            self.tweets_by_user[userId] = [(self.count, tweetId)]

    def getNewsFeed(self, userId: int) -> List[int]:
        # max_heap = []
        # heapq.heapify(max_heap)
        # loop through users following, then pick the latest tweets from each at most 10
        tweets = []
        
        users_following = self.following_by_user.get(userId, None)
        if users_following:
            for user in users_following:
                if user in self.tweets_by_user:
                    user_tweets = self.tweets_by_user[user]
                    tweets.extend(user_tweets)
                    

        if userId in self.tweets_by_user:
            tweets.extend(self.tweets_by_user[userId])

        tweets.sort()
        recent_tweets = tweets[-10:][::-1]
        return [tweetId[1] for tweetId in recent_tweets]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_by_user:
            self.following_by_user[followerId].add(followeeId)
        else:
            self.following_by_user[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_by_user and followeeId in self.following_by_user[followerId]:
            self.following_by_user[followerId].remove(followeeId)
        
