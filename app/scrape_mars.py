from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
 
def scrape_all_content():
     #initialize brower - chrome (in resources)
    browser = Browser("chrome", executable_path="../resources/chromedriver.exe", headless=False)

    news_title, news_para = mars_news(browser)
       #run all scraping functions and store in dictionary

    mars_data= {
        "news_title": news_title,
        "news_para" : news_para,
        "date_scrape": dt.datetime.now()
    }

    browser.quit()
    return mars_data

def mars_news(browser):
    #scrape for mars news url
    url = "https://mars.nasa.gov/news"
    browser.visit(url)

    browser.is_element_present_by_css('ul.item_list li.slide', wait_time=1)


    html = browser.html
    mars_news_soup = BeautifulSoup(html, "html.parser")

    try:
        # same as selecting bs; call (select_one)
        slide_element = mars_news_soup.select_one("ul.item_list li.slide")

        news_title = slide_element.find("div", class_="content_title").get_text()
        news_para = slide_element.find("div", class_="article_teaser_body").get_text() 
    except AttributeError:
        return None, None

    return news_title, news_para


# if __name__ == "__main__":
if __name__ == "__main__":
    # print scraped data
    print(scrape_all_content())
    
