# NKLCB Crawling gRPC

NKLCB Crawling gRPC는 테크 블로그 크롤링 서비스인 "네카라쿠배"의 gRPC 서버 애플리케이션입니다.

## Stack

- Python
- gRPC

for more information, see [requirements.txt](requirements.txt)

## Project Structure

- `proto/`: gRPC 프로토콜 버퍼 정의 파일 및 생성된 파일들
  - `crawling_service.proto`
  - `crawling_service_pb2.py`
  - `crawling_service_pb2_grpc.py`
- `src/`: 주요 소스 코드 디렉토리
  - `keyword_extractor.py`
  - `rss_parser.py`
  - `server.py`
  - `test_client.py`
- `requirements.txt`: 필요한 패키지 목록
- `.env`: 환경 변수 파일 (생성 후 추가)

## Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/kimday0326/nklcb-crawling-grpc.git
   ```
2. Move to the project directory
   ```sh
   cd nklcb-crawling-grpc
   ```
3. Create a `.env` file and add your API key
   ```sh
   echo "API_KEY=${YOUR_API_KEY}" > .env
   ```
4. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
5. Run the server
   ```sh
   python src/server.py
   ```
6. (Optional) If you want to test the client, open a new terminal and run the following command
   ```sh
   python src/test_client.py
   ```

## LICENSE

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
