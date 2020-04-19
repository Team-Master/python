from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

url = 'https://dhlottery.co.kr/common.do?method=main'
with urllib.request.urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    round = soup.find('strong', {'id': 'lottoDrwNo'}).text
    # print(round)
    all_spans = soup.find_all('span', {'class': 'ball_645'})
    # print(all_spans)
    # print(f'[/*{round}*/]')
    # print(f'[/*{round}*/ {",".join(all_spans)}]')
    # print(all_spans)
    numbers = []
    for span in all_spans:
        numbers.append(int(span.text))

# print(numbers)
print(f'/*{round}*/ {numbers}')
# r = requests.get(url)
# r.status_code