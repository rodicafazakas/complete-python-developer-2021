import requests
from bs4 import BeautifulSoup
import pprint

page = 0
all_links = []
all_subtext = []


# grab the data
while page < 3:

    res = requests.get('https://news.ycombinator.com/news?p='+str(page))
    # print(res.text)
    # clean the data
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup.body.contents)
    # print(soup.find_all('div'))
    links = soup.select('.storylink')
    subtext = soup.select('.subtext')
    # print(votes[0])
    #
    # for i in links:
    #     all_links.append(i)
    #
    # for i in subtext:
    #     all_subtext.append(i)

    all_links += links
    all_subtext += subtext
    page += 1

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(all_links, all_subtext))