"""
웹 주소(URI, URL)의 형식
프로토콜://서버주소[:포트번호]/경로?쿼리스트링
http://www.naver.com
https://comic.naver.com/webtoon/list.nhn?titleId=654774&weekday=mon
쿼리스트링(query string): 클라이언트(브라우저)가 서버로 보내는 정보
    param이름=param값 형식으로 작성
    파라미터가 여러개일 경우에는 &로 파라미터들 구분

다음에서 '머신러닝'으로 검색한 기사 100개의 URL 주소와 기사 제목을 출력
다음에서 임의의 검색어(키워드)로 검색한 기사 100개의 URL주소와 기사 제목을 출력하는 함수 작성하고 테스트
"""
import requests
from bs4 import BeautifulSoup


def get_news_title(keyword):
    # 접속 URL
    url = f'https://search.daum.net/search?w=news'
    for page in range(1, 11):
        print(f'===== Page {page} =====')
        req_params = {
            'q': keyword,
            'p': page
        }
        # 리퀘스트 넣어서 불러오기
        response = requests.get(url, params=req_params)
        # requests.getIurl, params={key, value}):
        #       params의 내용을 url의 query string의 파라미터로 추가해줌
        #       url?...&key=value
        html = response.text.strip()
        # 뷰티풀숲 객체 생성
        soup = BeautifulSoup(html, 'html5lib')

        news_link = soup.select('div.coll_cont a.f_link_b')
        for link in news_link:
            print(link.text, link.get('href'))


if __name__ == '__main__':
    keyword = input('검색 키워드를 입력하시오. >>')
    get_news_title(keyword)

    # for i in range(1, 11):
    #     print('===== Page', i)
    #     # 접속 URL
    #     url = f'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&p={i}'
    #     # 리퀘스트 넣어서 불러오기
    #     html = requests.get(url).text.strip()
    #     # 뷰티풀숲 객체 생성
    #     soup = BeautifulSoup(html, 'html5lib')
    #
    #     news_link = soup.select('div.coll_cont a.f_link_b')
    #     for link in news_link:
    #         print(link.text, link.get('href'))
