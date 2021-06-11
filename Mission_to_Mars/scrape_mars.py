from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def scrape_news():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit redplanetscience.com
    url = 'https://redplanetscience.com'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest mars news title and description
    articles = soup.find('div', class_='list_text')

    title = articles.find('div', class_='content_title').text
    descript = articles.find('div', class_='article_teaser_body').text

    # Close the browser after scraping
    browser.quit()

    # Return results
    return (title,descript)


def scrape_image():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit mars image url
    url = 'https://spaceimages-mars.com/image/news/img5.jpg'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the path to the image
    mars_image_path = soup.find('img')["src"]

    # Close the browser after scraping
    browser.quit()

    # Return results
    return url


def scrape_hemispheres():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit marshemispheres.com
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the image paths
    hemispheres = soup.find('div', class_='result-list')

    cerb_image = hemispheres.find_all('img')[0]["src"]
    cerb_image_path = url + cerb_image

    schiap_image = hemispheres.find_all('img')[1]["src"]
    schiap_image_path = url + schiap_image

    syrtis_image = hemispheres.find_all('img')[2]["src"]
    syrtis_image_path = url + syrtis_image

    valles_image = hemispheres.find_all('img')[3]["src"]
    valles_image_path = url + valles_image

    hemisphere_image_urls = [
        {"title": "Cerberus Hemisphere Enhanced", "img_url": cerb_image_path},
        {"title": "Schiaparelli Hemisphere Enhanced", "img_url": schiap_image_path},
        {"title": "Syrtis Major Hemisphere Enhanced", "img_url": syrtis_image_path},
        {"title": "Valles Marineris Hemisphere Enhanced", "img_url": valles_image_path}
    ]

    # Close the browser after scraping
    browser.quit()

    # Return results
    return hemisphere_image_urls

def scrape_all():

    title, descript = scrape_news()
    url = scrape_image()
    hemisphere_image_urls = scrape_hemispheres()

    data = {
        "news_title": title,
        "news_paragraph": descript,
        "featured_image": url,
        "hemispheres": hemisphere_image_urls,
    }

    return data