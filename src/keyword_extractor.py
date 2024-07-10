import os
import json
from dotenv import load_dotenv
import google.generativeai as genai


class KeywordExtractor:
    def __init__(self):
        self.__load_environment_variables()
        self.__configure_genai()

    def __load_environment_variables(self):
        load_dotenv(verbose=True)

    def __configure_genai(self):
        api_key = os.getenv("API_KEY")
        if api_key is None:
            raise ValueError(f"API key not found in environment variable")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def create_prompt(self, text):
        prompt = f"""다음 글의 요약과 메인 키워드(띄어쓰기, 특수문자 없이) 를 10개 추출하고 반환해줘. JSON 객체는 "summary"라는 50자 이내의 문자열과 "keywords"라는 키와 키워드 리스트를 포함해야 해.
        글:
        "{text}"
        응답 예시:
        {{
          "summary": "요약본",
          "keywords": ["키워드1", "키워드2"]
        }}"""
        return prompt

    def parse_response(self, response_text):
        response_text = response_text.strip().strip("```json").strip("```").strip()
        try:
            response_json = json.loads(response_text)
            summary = response_json.get("summary")
            keywords = response_json.get("keywords", [])
            return summary, keywords
        except json.JSONDecodeError:
            raise ValueError("Failed to decode JSON response")

    def generate_response(self, text):
        try:
            prompt = self.create_prompt(text)
            response = self.model.generate_content(prompt)
            return self.parse_response(response.text)
        except Exception as e:
            print(f"Failed to generate response: {e}")
            print(response.prompt_feedback)
            raise e


def main():
    text = """hello world"""
    extractor = KeywordExtractor()
    response = extractor.generate_response(text)
    print(response)


if __name__ == "__main__":
    main()
