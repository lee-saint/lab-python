from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open('web02.html', mode='r', encoding='UTF-8') as f:
        soup = BeautifulSoup(f, 'html5lib')
        # print(soup)

        # HTML 문서 안의 모든 div 태그 찾기
        for div in soup('div'):
            print(div.text)

        # HTML 문서 안의 'class1' 클래스 속성을 갖는 모든 요소 찾기
        # soup(attrs={attr이름: attr값})
        # soup.find_all(attrs={attr이름: attr 값})
        for cls_1 in soup(attrs={'class': 'class1'}):
            print(cls_1)

        # html 문서에서 'class2' 클래스 속성을 갖는 모든 요소 찾기
        for cls_2 in soup.find_all(class_='class2'):
            print(cls_2)

        # HTML 문서 안의 'id1' id 속성을 갖는 요소 찾기
        print(soup.find(attrs={'id': 'id1'}))
        print(soup.find(id='id1').text)
        print(soup(id='id1')[0].text)  # soup.find_all(id='id1')[0].text
