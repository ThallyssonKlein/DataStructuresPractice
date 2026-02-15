import unittest

# Se sua classe estiver em outro arquivo:
# from twitter import Twitter
from main import Twitter

class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()

    def test_example_case(self):
        self.twitter.postTweet(1, 5)
        self.assertEqual(self.twitter.getNewsFeed(1), [5])

        self.twitter.follow(1, 2)
        self.twitter.postTweet(2, 6)

        self.assertEqual(self.twitter.getNewsFeed(1), [6, 5])

        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [5])

    def test_feed_limit_10(self):
        for i in range(15):
            self.twitter.postTweet(1, i)

        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(len(feed), 10)
        self.assertEqual(feed, list(range(14, 4, -1)))

    def test_follow_multiple_users(self):
        self.twitter.postTweet(1, 1)
        self.twitter.postTweet(2, 2)
        self.twitter.postTweet(3, 3)

        self.twitter.follow(1, 2)
        self.twitter.follow(1, 3)

        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [3, 2, 1])

    def test_unfollow(self):
        self.twitter.postTweet(2, 10)
        self.twitter.follow(1, 2)

        self.assertEqual(self.twitter.getNewsFeed(1), [10])

        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [])

    def test_user_sees_own_tweets_without_following_self(self):
        self.twitter.postTweet(1, 100)
        self.assertEqual(self.twitter.getNewsFeed(1), [100])

    def test_unfollow_non_followed_user(self):
        # Não deve causar erro
        self.twitter.unfollow(1, 2)
        self.assertEqual(self.twitter.getNewsFeed(1), [])

    def test_tweets_order_across_users(self):
        self.twitter.postTweet(1, 5)
        self.twitter.postTweet(2, 6)
        self.twitter.postTweet(1, 7)
        self.twitter.postTweet(2, 8)

        self.twitter.follow(1, 2)

        feed = self.twitter.getNewsFeed(1)
        self.assertEqual(feed, [8, 7, 6, 5])

    def test_no_tweets(self):
        self.assertEqual(self.twitter.getNewsFeed(1), [])

    def test_multiple_follow_unfollow(self):
        self.twitter.postTweet(2, 20)
        self.twitter.postTweet(3, 30)

        self.twitter.follow(1, 2)
        self.twitter.follow(1, 3)
        self.assertEqual(self.twitter.getNewsFeed(1), [30, 20])

        self.twitter.unfollow(1, 3)
        self.assertEqual(self.twitter.getNewsFeed(1), [20])


if __name__ == "__main__":
    unittest.main()
