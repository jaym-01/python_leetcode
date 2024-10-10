class Twitter:

    def __init__(self):
        # stack of tweets
        self.tweets: list[tuple[int, int]] = []
        self.followers: dict[int, set[int]] = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        out = []
        for i in range(len(self.tweets) - 1, -1, -1):
            tweetId = self.tweets[i][1]
            usrTwtId = self.tweets[i][0]
            if len(out) < 10:
                if (userId in self.followers and usrTwtId in self.followers[userId]) or usrTwtId == userId:
                    out.append(tweetId)
            else:
                break
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followers:
            self.followers[followerId] = set([followeeId])
        else:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers and followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
