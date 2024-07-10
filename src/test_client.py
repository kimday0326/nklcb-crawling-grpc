import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "proto")))

import grpc
import crawling_service_pb2
import crawling_service_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = crawling_service_pb2_grpc.CrawlingServiceStub(channel)

        request = crawling_service_pb2.CrawlingRequest(
            rss_url="https://d2.naver.com/d2.atom",
            start_date_time="2024-06-27T00:00:00",
            end_date_time="2024-07-01T00:00:00",
        )

        response = stub.Crawl(request)

        for article in response.articles:
            print(f"Title: {article.title}")
            print(f"Author: {article.author}")
            print(f"Published At: {article.publishedAt}")
            print(f"Summary: {article.summary}")
            print(f"Keywords: {', '.join(article.keywords)}")
            print(f"Link: {article.link}")
            # print(f"Content: {article.content}")
            print("------------------------------------------------")


if __name__ == "__main__":
    run()
