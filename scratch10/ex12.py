"""
한겨레 신문사 페이지에서 특정 검색어 검색 결과 50개의 URL 주소, 기사 제목, 내용을 출력 -> 파일에 저장(txt)
1) URL 주소, 기사 제목 출력
2) 1) + 기사 내용 출력
3) 2)를 파일에 저장
"""
import requests
from bs4 import BeautifulSoup


def get_news_content(url):
    html = requests.get(url).text.strip()
    soup = BeautifulSoup(html, 'html5lib')

    news_contents = soup.select('div.article-text div.text')
    print(news_contents[0].text.strip())


def hani_news_search(keyword):
    url = 'http://search.hani.co.kr/Search?command=query&media=news&sort=d&period=all'
    for page in range(5):
        req_params = {
            'keyword': keyword,
            'pageseq': page
        }
        response = requests.get(url, params=req_params)
        html = response.text.strip()
        soup = BeautifulSoup(html, 'html5lib')

        news_links = soup.select('ul.search-result-list dt a')
        for link in news_links:
            news_title = link.text
            news_url = link.get('href')
            print(news_title, news_url)
            get_news_content(news_url)


if __name__ == '__main__':
    hani_news_search('머신러닝')
