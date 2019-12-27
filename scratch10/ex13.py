"""
icrawler 패키지 사용해서 Google 이미지 검색 결과의 이미지 다운로드
> pip install icrawler
"""
from icrawler.builtin import GoogleImageCrawler
import os

if __name__ == '__main__':
    # 이미지 저장 경로
    save_dir = os.path.join('C:' + os.sep, 'dev', 'images')
    # GoogleImageCrawler 객체 생성
    google_crawler = GoogleImageCrawler(storage={'root_dir': save_dir})

    # 검색 필터링(filter) 조건
    filters = {
        'size': 'large',
        'license': 'noncommercial,modify',
        'color': 'blackandwhite'
    }

    google_crawler.crawl(keyword='cat', filters=filters, max_num=50)
