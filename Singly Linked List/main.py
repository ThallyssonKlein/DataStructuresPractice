from typing import List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, value):
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_at_beginning(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


class Twitter:
    def __init__(self):
        self.linkedListPosts = LinkedList()
        self.hashMapUserIdTweetId = {}
        self.hashMapUserFollows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.linkedListPosts.insert_at_beginning(tweetId)
        self.hashMapUserIdTweetId[tweetId] = userId

    def getNewsFeed(self, userId: int) -> List[int]:
        arr = []
        current = self.linkedListPosts.head
        while current:
            if len(arr) == 10:
                return arr

            userIdTweet = self.hashMapUserIdTweetId[current.value]
            if userIdTweet == userId:
                arr.append(current.value)
                current = current.next
                continue

            userFollows = self.hashMapUserFollows[userId]
                
            if userIdTweet in userFollows:
                arr.append(current.value)
            current = current.next
        
        return arr


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return

        try:
            self.hashMapUserFollows[followerId].add(followeeId)
        except:
            self.hashMapUserFollows[followerId] = {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        try:
            self.hashMapUserFollows[followerId].discard(followeeId)
        except:
            pass


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)