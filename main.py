import random
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
# from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from Searcher import SearchGenerator

options = EdgeOptions()
# options = ChromeOptions()
options.add_experimental_option("detach", True)
# options.add_experimental_option("debuggerAddress", "localhost:8989")
# options.add_argument("user-data-dir=C:\\Users\\krish\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")

# starting the driver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
# driver = webdriver.Chrome(options=options)
driver.maximize_window()


def make_browser_search(query):
    driver.get('https://www.bing.com/')
    time.sleep(3)
    search_box = driver.find_element(By.ID, 'sb_form_q')
    search_box.send_keys(query, Keys.ENTER)


# TODO 1. Add CLI arguments to pass the no. of searches and also specifying the browser to use
if __name__ == '__main__':
    searcher = SearchGenerator()
    i = 0
    for headline in searcher.generate_searches():
        i += 1
        search = " ".join(headline.split()[:random.randint(4, 7)])
        make_browser_search(search)
        time.sleep(2)
        print(f"\rNo of searches done : {i}", end="", sep="")

