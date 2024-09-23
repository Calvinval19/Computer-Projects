import sys
import requests
from bs4 import BeautifulSoup
import random

def scrapeWikiArticle(url):
    try:
        response =requests.get(
            url=url,
        )
    except requests.exceptions.RequestException as e:
        print('All done!')
        sys.exit(0)
    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find(id= "firstHeading")
    print(title.text) 

    # Get all the links
    allLinks = soup.find(id= "bodyContent").find_all("a")
    random.shuffle(allLinks)
    linkToScrape = 0

    for link in allLinks:
        # We are only interested in other wiki articles
        if link['href'].find("/wiki/") == -1:
            continue
        # Use this link to scrape
        linkToScrape = link
        break
        
    scrapeWikiArticle("https://en.wikipedia.org" + linkToScrape['href'])

def main():
    website = input('Enter the wikipedia website you would like to scrape\n')
    scrapeWikiArticle(website)


main()
