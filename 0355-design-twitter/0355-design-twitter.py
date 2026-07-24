class Twitter:
    def __init__(self):
        self.count=0
        self.followmap=defaultdict(set)
        self.tweetsmap=defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetsmap[userId].append([self.count, tweetId])
        self.count-=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        max_heap=[]
        self.followmap[userId].add(userId)

        for followee in self.followmap[userId]:
            if len(self.tweetsmap[followee])>0:
                index=len(self.tweetsmap[followee])-1
                count, tweetId= self.tweetsmap[followee][index]
                heapq.heappush(max_heap, (count, tweetId, followee, index-1))

        while max_heap and len(res)<10:
            count, tweetId, followee, index= heapq.heappop(max_heap)
            res.append(tweetId)
            if index>=0:
                count, tweetId= self.tweetsmap[followee][index]
                heapq.heappush(max_heap, (count, tweetId, followee, index-1))

        return res
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)