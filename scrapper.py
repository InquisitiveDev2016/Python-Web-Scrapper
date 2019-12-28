import urllib.request
from bs4 import BeautifulSoup as soup
import requests

url = 'https://unsplash.com/s/photos/download'

def download_imgs(url, amountOfImgs):
    req=requests.get(url, allow_redirects=True)
    html=req.text
    #parsing the html from the url
    page_soup = soup(html, "html.parser")
    images = [img for img in page_soup.findAll('img')]
    counter = 0
    #compiling the unicode list of image links
    image_links = [each.get('src') for each in images]
    #removing all duplicate links from list by converting to set
    image_links_toSet = set(image_links)
    #turning it back to a list and filtering out all null values
    img_links = list(filter(None, image_links_toSet))

    #downloading images from each extracted img src url
    #naming img files based on current counter
    for each in img_links:
        
        if(counter < amountOfImgs):
            filename = 'img' + str(counter) + '.jpg'
            urllib.request.urlretrieve(each, filename)
            print(filename)
            counter += 1
        else:     
            return img_links


#Can specify amount of images you would like to download in the second parameter of the function
download_imgs(url, 10)


#https://images.unsplash.com/photo-1550028061-1de66…hcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=800&q=60
