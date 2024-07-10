import grpc
from concurrent import futures
import time
import logging
import crawling_service_pb2
import crawling_service_pb2_grpc
from keyword_extractor import KeywordExtractor
from rss_parser import RSSParser

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class CrawlingServiceServicer(crawling_service_pb2_grpc.CrawlingServiceServicer):
    def Crawl(self, request, context):
        logging.info(f"Received request with RSS link: {request.rss_url}")
        rss_parser = RSSParser(request.rss_url)
        extractor = KeywordExtractor()

        logging.info(f"Start crawling from {request.start_date_time} to {request.end_date_time}")
        logging.info("-" * 50)
                
        articles = []
        for entry in rss_parser.feed_list:
            article = rss_parser.parse_article(entry, extractor, request.start_date_time, request.end_date_time)
            if article:
                articles.append(article)
                logging.info(f"Crawled article: {article.title}")
                time.sleep(1)

        logging.info("Crawling finished")
        logging.info("-" * 50)
        return crawling_service_pb2.CrawlingResponse(articles=articles)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crawling_service_pb2_grpc.add_CrawlingServiceServicer_to_server(CrawlingServiceServicer(), server)
    
    server.add_insecure_port('[::]:50051')
    logging.info("Server started on port 50051")
    server.start()

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
