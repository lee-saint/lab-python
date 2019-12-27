import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 접속할 사이트(웹 서버) 주소
    url = 'https://search.daum.net/search?w=news&q=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&DA=YZR&spacing=0'

    # 사이트(웹 서버)로 요청(request) 보내기
    html = requests.get(url).text.strip()  # 요청의 결과(응답, response - HTML)를 저장
    # print(html[:100])  # 전체 문자열에서 100자만 확인

    # HTML 문서의 모든 링크에 걸려 있는 주소들을 출력
    soup = BeautifulSoup(html, 'html5lib')
    # print(soup)
    for link in soup('a'):
        print(link.get('href'))
    print()

    # 관심 있는 링크(뉴스 링크)만 찾을 수 있는 방법을 고민
    newscoll = soup.find(id='newsColl')
    coll_content = soup.find(class_='coll_cont')
    for link in coll_content('a', class_='f_link_b'):
        print(link.get('href'))

    div_coll_cont = soup.find_all(class_='coll_cont')
    print(len(div_coll_cont))
    # HTML 하위 요소(sub/child element)를 찾는 방법:
    # 1) parent_selector > child_selector
    #       div > ul > li
    #       .coll_cont > #clusterResultul > .fst
    # 2) ancestor_selector(조상 선택자) descendant_selector(자손 선택자)
    #       div li(div의 자손 요소 중 li)
    #       .coll_cont .fst(클래스 .coll_cont 요소의 자손 요소들 중 클래스가 .fst인 요소들
    # soup.select(css_selector): css 객체에서 CSS 선택자로 요소들을 찾는 방법
    news_link = soup.select('.coll_cont ul li a.f_link_b')
    for link in news_link:
        print(link.get('href'))
