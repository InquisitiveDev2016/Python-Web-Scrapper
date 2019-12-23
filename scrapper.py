import urllib.request
from bs4 import BeautifulSoup as soup
import requests

url = 'https://unsplash.com/s/photos/download'



def download_imgs(url, amountOfImgs):
    req=requests.get(url)
    html=req.text
    #parsing the html from the url
    page_soup = soup(html, "html.parser")
    images = [img for img in page_soup.findAll('img')]
    counter = 0
    #compiling the unicode list of image links
    image_links = [each.get('src') for each in images]

    for each in image_links:
        if(counter <= amountOfImgs):
            filename = each.split('/')[-1]
            urllib.request.urlretrieve(each, filename)
            counter += 1
        else:
            return image_links




download_imgs(url, 5)
