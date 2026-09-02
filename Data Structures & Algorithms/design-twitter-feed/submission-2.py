from collections import deque
class Twitter:

    def __init__(self):
        self.tweetQueue = deque()
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetQueue.append([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        ret = []
        tweets = 0
        i = len(self.tweetQueue) - 1
        if self.tweetQueue:
            while i > -1 and tweets < 10:
                if userId == self.tweetQueue[i][0] or (userId in self.following and self.tweetQueue[i][0] in self.following[userId]):
                    ret.append(self.tweetQueue[i][1])
                    tweets += 1
                i -= 1
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if (not followerId in self.following) or not followeeId in self.following[followerId]:
            if followerId not in self.following:
                self.following[followerId] = set()
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            if followeeId in self.following[followerId]:
                self.following[followerId].remove(followeeId)
        
        
