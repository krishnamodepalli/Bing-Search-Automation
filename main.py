import os
import random
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from SearchGenerator import SearchGenerator


class BrowserCodes:
    CHROME = 1
    BRAVE = 2
    EDGE = 3

    def get_browser(self, code) -> str:
        if code == 1:    res = 'chrome'
        elif code == 2:  res = 'brave'
        elif code == 3:  res = 'edge'
        else:
            raise Exception(f'Unknown code {code} parsed. Please correct the '
                            f'code you sent')
        return res


# Kindly, please change the below configurations for your use-case and browsers
app_configuration = {
    'browser': 'chrome',
    'port': 8989,
    'chrome-profile-dir': r'C:\Users\krish\Apps\chrome\profile',
    'search-count': 10
}

driver = None


# To open the browser and then open the bing search engine
def set_browser_ready(browser: int) -> None:
    """Open the specified browser and opens the bing website."""
    # open the browser with the remote debugging mode and then attach to browser

    global driver
    if browser in [1, 2]:           # chrome or brave
        # chrome and brave are well suited with debugging modes for our project
        options = ChromeOptions()
        # starting the browser
        os.system(
            f'start chrome --remote-debugging-port={app_configuration["port"]} \
            --user-data-dir="{app_configuration["chrome-profile-dir"]}"')
        # attaching the driver to the browser
        options.add_experimental_option("debuggerAddress", "localhost:8989")
        driver = webdriver.Chrome(options=options)
    elif browser == 3:              # edge
        options = EdgeOptions()
        # not closing the browser after completion of the task
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    driver.get('https://www.bing.com/')


def make_browser_search(query: str) -> None:
    """
    While the driver is still on the bing website, this method will go to the
    search bar and will search for the query given as an argument
    :param query: The query or the search to be searched in the bing website
    :return: None
    """
    # TODO 2: Make sure the driver is ready with the bing website
    time.sleep(3)
    search_box = driver.find_element(By.ID, 'sb_form_q')
    # if the search-box is not clear, clear it.
    search_box.clear()
    search_box.send_keys(query, Keys.ENTER)


# TODO 1. Add CLI arguments to pass the no. of searches and also specifying the browser to use
if __name__ == '__main__':
    generator = SearchGenerator()
    set_browser_ready(BrowserCodes.CHROME)
    i = 0
    for headline in generator.generate_searches(
            app_configuration['search-count']):
        i += 1
        search = " ".join(headline.split()[:random.randint(4, 7)])
        make_browser_search(search)
        time.sleep(2)
        print(f"\rNo of searches done : {i} ✔", end="", sep="")
