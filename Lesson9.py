import requests
from bs4 import BeautifulSoup

siteDate = requests.get('https://coinmarketcap.com/')
# print(siteDate.text)

# siteParsed = list(siteDate.text.split('<span>'))
# index = 0
# for item in siteParsed:
#     index += 1
#     print(f'{index}-> : {siteParsed}')
# print(siteParsed[1])

print(siteDate.status_code)

siteSoup = BeautifulSoup(siteDate.text, features='html.parser')
# <div class="sc-9d064f2d-0 cAhksY rise"><span>$66,943.14</span></div>

rates = siteSoup.find_all(name='div', attrs={'class': 'sc-9d064f2d-0'})
# for rate in rates:
#     print(rate.find('span').text)

# <p font-weight="semibold" color="text" font-size="1" data-sensors-click="true" class="sc-4984dd93-0 kKpPOn">Bitcoin</p>
names = siteSoup.find_all(name='p', attrs={'class': 'kKpPOn'})

for name in names:
    print(name.text)
