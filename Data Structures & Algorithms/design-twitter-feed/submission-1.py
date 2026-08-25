class Twitter:

    def __init__(self):
        self.tweets_by_user = {} #{user: [(counter, tweetId)]}
        self.following_by_user = {} #{user: {following set()}}
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # attach counter to each tweets - to track the latest tweets.
        if userId in self.tweets_by_user:
            self.tweets_by_user[userId].append((self.count, tweetId))
        else:
            self.tweets_by_user[userId] = [(self.count, tweetId)]

        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        heapq.heapify(min_heap)
        # loop through users following, then pick the latest tweets from each at most 10

        res = []
        
        if userId in self.following_by_user:
            self.following_by_user[userId].add(userId)
        else:
            self.following_by_user[userId] = {userId}
        
        for user in self.following_by_user[userId]:
            if user in self.tweets_by_user:
                index = len(self.tweets_by_user[user]) - 1
                counter, tweetId = self.tweets_by_user[user][index]
                heapq.heappush(min_heap, [counter, tweetId, user, index])

        while min_heap and len(res) < 10:
            counter, tweetId, user, index = heapq.heappop(min_heap)
            res.append(tweetId)

            index -= 1
            if index >= 0:
                counter, tweetId = self.tweets_by_user[user][index]
                heapq.heappush(min_heap, [counter, tweetId, user, index])    

        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_by_user:
            self.following_by_user[followerId].add(followeeId)
        else:
            self.following_by_user[followerId] = {followeeId}
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following_by_user and followeeId in self.following_by_user[followerId]:
            self.following_by_user[followerId].remove(followeeId)
        
