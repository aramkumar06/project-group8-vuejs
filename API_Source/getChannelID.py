from urllib.request import urlopen, unquote
from bs4 import BeautifulSoup as BS


input_URL = 'https://www.youtube.com/user/Mnet'
URL = input_URL

html = urlopen(URL).read()
soup = BS(html, "html.parser", from_encoding='utf-8')
ff = soup.find_all("button", attrs={'class': "yt-uix-button yt-uix-button-size-default "
                                             "yt-uix-button-subscribe-branded yt-uix-button-has-icon "
                                             "no-icon-markup yt-uix-subscription-button yt-can-buffer"})
youtubeID = ff[0].get('data-channel-external-id')
print(youtubeID)

li_tags = soup.find_all("li", attrs={'class': "channel-links-item"})
for li_tag in li_tags:
    before_link = li_tag.find('a').get('href')
    link = unquote(before_link[before_link.find('http'):])
    if '&' in link:
        link = link[:link.find('&')]
    print(link)
