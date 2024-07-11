import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "proto")))

import grpc
import crawling_service_pb2
import crawling_service_pb2_grpc

from concurrent import futures
import time
from keyword_extractor import KeywordExtractor
from rss_parser import RSSParser

os.environ["GRPC_VERBOSITY"] = "ERROR"
os.environ["GRPC_TRACE"] = ""


class CrawlingServiceServicer(crawling_service_pb2_grpc.CrawlingServiceServicer):
    def Crawl(self, request, context):
        print(f"Received request with RSS link: {request.rss_url}")
        rss_parser = RSSParser(request.rss_url)
        extractor = KeywordExtractor()

        print(
            f"Start crawling from {request.start_date_time} to {request.end_date_time}"
        )
        print("-" * 50)

        articles = []
        for entry in rss_parser.feed_list:
            article = rss_parser.parse_article(
                entry, extractor, request.start_date_time, request.end_date_time
            )
            if article:
                articles.append(article)
                print(f"Crawled article: {article.title}")
                time.sleep(1)

        print("Crawling finished")
        print("-" * 50)
        return crawling_service_pb2.CrawlingResponse(articles=articles)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crawling_service_pb2_grpc.add_CrawlingServiceServicer_to_server(
        CrawlingServiceServicer(), server
    )

    server.add_insecure_port("[::]:50051")
    print("Server started on port 50051")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
