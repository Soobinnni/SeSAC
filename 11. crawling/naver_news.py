import requests
from bs4 import BeautifulSoup

naver_sports = 'https://sports.news.naver.com/index.nhn'
naver_land = 'https://land.naver.com/news/'

def get_requests_html_parser(url) :
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    return soup

def get_news_info() :
    soup = get_requests_html_parser(naver_sports)
    news_text = soup.select('.today_list > li')

    news_info = []
    news ={}
    for n in news_text :
        # news['title'] = n.select('.text_area > strong')[0].text.strip()
        # news['title'] = n.select('.text_area > .title')[0].text.strip()
        news['title'] = n.select('a')[0]['title'].strip()
        news_info.append(news)
        print(news)
        
def get_land_info(type) :
    types = ['headline', 'headline_content', 'report']
    if type not in types :  
        return print("Unknow Type")

    soup = get_requests_html_parser(naver_land)
    if type == 'headline' :
        return get_headline_text(soup)
    
    if type == 'headline_content' :
        soup = get_requests_html_parser(naver_land)
        return get_headline_content(soup)
    
    if type == 'report' :
        soup = get_requests_html_parser(naver_land)
        return get_report_text(soup)


def get_headline_text(soup) :
    land_text = soup.select('.section_group:first-child > ul.list_type > li a:nth-child(2)')
    for l in land_text :
        print(f'headline : {l.text}')

def get_report_text(soup) :
    uls = soup.select('.section_group:last-child > ul')
    for ul in uls :
        a = [a.text for a in ul.select('.list_type > li a')]
        for report_content in a:
            print(f'report_content : {report_content}')

def get_headline_href(soup) :
    land_text = soup.select('.section_group:first-child > ul.list_type > li a:nth-child(2)')
    content_url_list = ['https://land.naver.com' + l.attrs['href'] for l in land_text]

    return content_url_list

def get_headline_content(soup) :
    content_url_list = get_headline_href(soup)

    for url in content_url_list :
        soup = get_requests_html_parser(url)
        content = soup.select_one('#articleBody').text
        print(f'content : content')

# 미션 3. 저 헤드라인 기사의 본문을 가져오기

if __name__ == '__main__' :
    # get_news_info()
    # get_land_info('headline')
    # get_land_info('report')
    # get_land_info('reporadsft')
    get_land_info('headline_content')