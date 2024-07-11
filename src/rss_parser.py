import feedparser
import time
import crawling_service_pb2


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

    def parse_article(self, entry, extractor, start_date_time, end_date_time):
        published_at = time.strftime(
            "%Y-%m-%dT%H:%M:%S",
            entry.get("published_parsed") or entry.get("updated_parsed"),
        )

        if start_date_time < published_at < end_date_time:
            content = None
            if "content" in entry:
                if isinstance(entry["content"], list) and len(entry["content"]) > 0:
                    content = entry["content"][0].value
                else:
                    content = entry["content"]
            else:
                content = entry.get("summary")

            if content is None:
                print(f"Error extracting content from entry: {entry}")
                return None

            summary, keywords = extractor.generate_response(content)

            article = crawling_service_pb2.Article(
                title=entry.get("title"),
                summary=summary,
                content=content,
                author=entry.get("author")
                or entry.get("creator")
                or entry.get("dc:creator"),
                link=entry.get("link"),
                publishedAt=published_at,
                keywords=keywords,
            )
            return article
        return None
