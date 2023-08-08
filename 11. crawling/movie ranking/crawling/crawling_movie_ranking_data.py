import requests
from bs4 import BeautifulSoup
from datetime import date

daum_movie = 'https://movie.daum.net/ranking/reservation'

def get_requests_html_parser(url) :
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    return soup

def get_li_element_with_data() :
    domain_soup = get_requests_html_parser(daum_movie)
    li = domain_soup.select('ol.list_movieranking')[0].select('li')

    return li 

def mk_movie_rank_info_list() :
    li = get_li_element_with_data()
    movie_rank_infos = []
    for i, l in enumerate(li) :
        movie_rank_info = {}
        movie_rank_info['title'] =  l.select_one('.tit_item a').text.strip()
        movie_rank_info['ranking'] = (i+1)
        movie_rank_info['post_url'] = l.select_one('.thumb_item > div.poster_movie > img').attrs['src'].strip()
        movie_rank_info['short_description'] = l.select_one('.poster_info a').text.strip()
        movie_rank_info['link'] = 'https://movie.daum.net'+(l.select_one('.poster_info a').attrs['href'].strip())
        movie_rank_info['link'] = 'https://movie.daum.net'+(l.select_one('.poster_info a').attrs['href'].strip())
        movie_rank_info['date'] =  str(date.today())
        movie_rank_info['rating'] = float(l.select_one('span.txt_append > span:nth-child(1) > span').text.strip())
        movie_rank_info['reservation_rate'] = float(l.select_one('span.txt_append > span:nth-child(2) > span').text.strip().split("%")[0])

        movie_rank_infos.append(movie_rank_info)

    return movie_rank_infos