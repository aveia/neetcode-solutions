# design twitter
# https://neetcode.io/problems/design-twitter-feed/question
# code by aveia@github

class Twitter:

    def __init__(self):
        from collections import defaultdict, deque
        self.tweets = defaultdict(deque)
        self.followed = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        userTweets = self.tweets[userId]
        userTweets.appendleft(tweetId)
        if len(userTweets) > 10:
            userTweets.pop()

    def getNewsFeed(self, userId: int) -> list[int]:
        import heapq
        tweets = self.tweets[userId]
        for followee in self.followed[userId]:
            tweets = heapq.merge(tweets, self.tweets[followee], reverse=True)
        return list(tweets)[:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followed[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followed[followerId]:
            self.followed[followerId].remove(followeeId)
