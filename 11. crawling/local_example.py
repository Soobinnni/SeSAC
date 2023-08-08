from bs4 import BeautifulSoup

html = '''
    <div class="link_news">
        <h3>헤럴드경제 관련뉴스
            <span>해당 언론사에 서 선정하며 <em>언론사 페이지(아웃링크)</em>로 이동해 볼 수 있습니다.</span>
        </h3>
        <ul>
            <li>
                <a href="http://biz.heraldcorp.com/view.php?ud=20230804000112&amp;pos=naver" target="_blank">'윤석열 굿즈', 이르면 올 추석부터 용산어린이정원서 판매한다</a>
            </li>
            <li>
                <a href="http://biz.heraldcorp.com/view.php?ud=20230804000144&amp;pos=naver" target="_blank">48세 명세빈 동안 비결 공개…"보톡스 옅은 농도로"</a>
            </li>
            <li>
                <a href="http://biz.heraldcorp.com/view.php?ud=20230804000233&amp;pos=naver" target="_blank">블랙핑크 제니, 직접 디자인한 포르쉐 슈퍼카 공개</a>
            </li>
            <li>
                <a href="http://biz.heraldcorp.com/view.php?ud=20230804000238&amp;pos=naver" target="_blank">심형탁, 처가 빈손 방문 비판에…"괴물로 만들지 말라"</a>
            </li>
            <li>
                <a href="http://biz.heraldcorp.com/view.php?ud=20230803000515&amp;pos=naver" target="_blank">"손주 보러온 어머니 사우나 이용금지" 강남아파트는 왜 커뮤니티 이용을 막았나 [부동산360]</a>
            </li>
        </ul>
    </div> 
'''
soup = BeautifulSoup(html, 'html.parser') # 직접 작성하여 연습할 수도 있음
div_link_news = soup.find('div', class_='link_news') # div요소 중 class 이름이 link_news인 것을 찾는다
lis = div_link_news.find_all('li') #모든 li태그들을 찾는다.