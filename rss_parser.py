import feedparser

class RSSParser:
    def __init__(self, rss_url):
        self.rss_url = rss_url
        self.feed_list = self.parse_rss()

    def parse_rss(self):
        try:
            feed = feedparser.parse(self.rss_url)
            return feed.entries
        except Exception as e:
            print(f"Error fetching RSS feed: {e}")
            return None
