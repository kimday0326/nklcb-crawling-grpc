import grpc
from concurrent import futures
import time
import crawling_service_pb2
import crawling_service_pb2_grpc
from rss_parser import RSSParser
from keyword_extractor import KeywordExtractor

class CrawlingServiceServicer(crawling_service_pb2_grpc.CrawlingServiceServicer):
    def Crawl(self, request, context):
        print(f"Received request with RSS link: {request.rss_url}")
        rss_parser = RSSParser(request.rss_url)
        # base_time = time.strptime(request.base_time, '%Y-%m-%dT%H:%M:%S')
        extractor = KeywordExtractor()
        print(request.base_time)
        
        articles = []
        for entry in rss_parser.feed_list:
            publised_at = time.strftime('%Y-%m-%dT%H:%M:%S',entry.get('published_parsed') or entry.get('updated_parsed'))
            # print(entry.get('title'))
            print(publised_at, request.base_time)
            if publised_at > request.base_time:
                print(publised_at > request.base_time)
                content = entry.get('content.value') or entry.get('summary')
                summary, keywords = extractor.generate_response(content)
                article = crawling_service_pb2.Article(
                    title=entry.get('title'),
                    summary=summary,
                    content=content,
                    author=entry.get('author') or entry.get('creator') or entry.get('dc:creator'),
                    link = entry.get('link'),
                    publishedAt=publised_at,
                    keywords=keywords,
                )
                articles.append(article)
                time.sleep(1)

        return crawling_service_pb2.CrawlingResponse(articles=articles)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crawling_service_pb2_grpc.add_CrawlingServiceServicer_to_server(CrawlingServiceServicer(), server)
    
    print("Server started on port 50051")
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()