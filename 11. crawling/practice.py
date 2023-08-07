import requests
from bs4 import BeautifulSoup

data = requests.get('https://www.pythonscraping.com/pages/page3.html')

# print(data.text) # html태그들이 출력된다.

soup = BeautifulSoup(data.text, 'html.parser')

# 1) table을 가져온다
# gifts = soup.select('#giftList')
# print(gifts)

# 2) table의 tr을 가져온다
gifts = soup.select('#giftList > tr')
#print(gifts)
#print(len(gifts)) # tr의 개수를 센다
my_gifts = gifts[1:] # header는 필요 없음

gift_info = []
gift ={}
for g in my_gifts :
    #print(g)
    tds = g.select('td')
    gift['title'] = tds[0].text.strip()
    gift['price'] = tds[2].text.strip()
    gift['img'] = tds[3].img['src'].strip()
    gift_info.append(gift)

print(gift_info)
