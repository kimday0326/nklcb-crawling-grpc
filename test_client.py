import grpc
import crawling_service_pb2
import crawling_service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crawling_service_pb2_grpc.CrawlingServiceStub(channel)

        request = crawling_service_pb2.CrawlingRequest(
            rss_url='https://d2.naver.com/d2.atom',
            base_time='2024-07-02T00:00:00'
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

if __name__ == '__main__':
    run()