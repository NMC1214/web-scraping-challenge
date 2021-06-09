from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


def scrape_news():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit MarsFacts.com
    url = 'https://redplanetscience.com'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest mars news title and description
    articles = soup.find('div', class_='list_text')
    
    title = articles.find('div',class_='content_title').text
    descript = articles.find('div',class_='article_teaser_body').text

    # Store data in a dictionary
    mars_news_data = {
        "Mars News": title,
        "News Summary": descript
    }

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_news_data

def scrape_image():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit MarsFacts.com
    url = 'https://spaceimages-mars.com/image/news/img5.jpg'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest mars news title and description
    mars_image_path = soup.find('img')["src"]

    # Close the browser after scraping
    browser.quit()

    # Return results
    return mars_image_path

def scrape_hemispheres():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit MarsFacts.com
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

    # Get the latest mars news title and description
    hemispheres = soup.find('div', class_='result-list')
    cerb_image = hemispheres.find_all('img')[0]["src"]
    cerb_image_path = url + cerb_image
    cerb_title = hemispheres.find_all('img')[0]["alt"]

    schiap_image = hemispheres.find_all('img')[1]["src"]
    schiap_image_path = url + schiap_image
    schiap_title = hemispheres.find_all('img')[1]["alt"]

    syrtis_image = hemispheres.find_all('img')[2]["src"]
    syrtis_image_path = url + syrtis_image
    syrtis_title = hemispheres.find_all('img')[2]["alt"]

    valles_image = hemispheres.find_all('img')[2]["src"]
    valles_image_path = url + valles_image
    valles_title = hemispheres.find_all('img')[2]["alt"]
    
    hemisphere_image_urls = [
        {"title": cerb_title, "img_url": cerb_image_path},
        {"title": schiap_title, "img_url": schiap_image_path},
        {"title": syrtis_title, "img_url": syrtis_image_path},
        {"title": valles_title, "img_url": valles_image_path},
    ]

    # Close the browser after scraping
    browser.quit()

    # Return results
    return hemisphere_image_urls

