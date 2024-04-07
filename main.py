import argparse
import os
import random as rn
import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from SearchGenerator import SearchGenerator


class BrowserCodes:
    """
    A simple struct like light-weight class for just converting browser-codes
    into browser-names (str) and vice-versa. Just making it convenient for
    knowing browser-code for each browser.
    """
    CHROME = 1
    BRAVE = 2
    EDGE = 3

    @staticmethod
    def get_browser(code: str) -> int:
        """
        This will provide the browser name for the corresponding browser code.
        :return browser_name: int value of the browser name
        """
        if code == 'chrome':
            res = 1
        elif code == 'brave':
            res = 2
        elif code == 'edge':
            res = 3
        else:
            raise Exception(f'Unknown code {code} parsed. Please correct the '
                            f'code you sent')
        return res


# Kindly, please change the below configurations for your use-case and browsers
# Not all the configurations are always used for the application, only some
# are used based on specifications and needs. 'chrome-profile-dir' and others
# are used for Chrome browser. Only the search-count is always used.
app_configuration = {
    'search-source': 'keywords',  # this field can be 'keywords' or 'news-api'
    'browser': 'chrome',
    'port': 8989,
    'chrome-profile-dir': r'C:\Users\krish\Apps\chrome\profile',
    'search-count': 30
}

driver = None


# To open the browser and then open the bing search engine
def set_browser_ready(browser: int) -> None:
    """Open the specified browser and opens the bing website."""
    # open the browser with the remote debugging mode and then attach to browser

    global driver
    if browser in [1, 2]:  # chrome or brave
        # chrome and brave are well suited with debugging modes for our project
        options = ChromeOptions()
        # starting the browser
        if browser == 1:
            brow = 'chrome'         # the browser to use
        else:
            brow = 'brave'
        os.system(
            f'start {brow} --remote-debugging-port={app_configuration["port"]} \
            --user-data-dir="{app_configuration["chrome-profile-dir"]}"')
        # attaching the driver to the browser
        options.add_experimental_option("debuggerAddress", "localhost:8989")
        driver = webdriver.Chrome(options=options)
    elif browser == 3:  # edge
        print('You called edge')
        # mobile_emulation = {
        #     "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
        #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 "
        #                  "Build/JOP40D) AppleWebKit/535.19 (KHTML, "
        #                  "like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
        # }
        options = EdgeOptions()
        # options.add_experimental_option('mobileEmulation', mobile_emulation)
        # not closing the browser after completion of the task
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)

    driver.maximize_window()
    driver.get('https://www.bing.com/')
    # it is better to wait for the webpage to load
    time.sleep(2.0)


def make_browser_search(query: str) -> None:
    """
    While the driver is still on the bing website, this method will go to the
    search bar and will search for the query given as an argument
    :param query: The query or the search to be searched in the bing website
    :return: None
    """
    # TODO 2: Make sure the driver is ready with the bing website
    search_box = driver.find_element(By.ID, 'sb_form_q')
    # if the search-box is not clear, clear it.
    search_box.clear()
    search_box.send_keys(query, Keys.ENTER)


def make_multiple_searches(searches: [str], search_gap: float = 2.0) -> None:
    """
    This method automates the work of making each search individually
    :param searches A list of strings(queries or searches) to be searched
    :param search_gap Time gap between each search to be made, (in float).
    :return None
    """
    search_count = 0
    for search_query in searches:
        make_browser_search(search_query)
        search_count += 1
        print(f"\rNo of searches done : {search_count} ✔", end="", sep="")
        time.sleep(search_gap)


# TODO 1. Add CLI arguments to pass the no. of searches and also specifying
#  the browser to use
if __name__ == '__main__':
    # arg-parser
    parser = argparse.ArgumentParser(
        prog='main.py',
        description='Automates the task of making bing searches and earning \
bing reward points.',
        epilog='Some ending text')

    parser.add_argument('-c', '--search-count',
                        type=int, default=30)
    parser.add_argument('-b', '--browser',
                        choices=['chrome', 'edge', 'brave'], type=str,
                        default='chrome')
    parser.add_argument('-g', '--search-gap', type=float, default=2.0)
    parser.add_argument('-t', '--search-type', type=int, choices=[1, 2],
                        help="1 for keywords and 2 for news-api highlights",
                        default=1)

    args = parser.parse_args()
    set_browser_ready(BrowserCodes.get_browser(args.browser or
                                               app_configuration['browser']))

    no_of_searches = args.search_count
    searching_type = args.search_type
    search_gap = args.search_gap

    if searching_type == 1:     # keywords
        with open('./keywords.txt', 'r') as keywords_file:
            # randomly generate a large number and then extract 30 lines from it
            n = rn.randint(1, 10000)
            lines = keywords_file.readlines()[n:n + no_of_searches]
            make_multiple_searches(lines, search_gap)
    elif searching_type == 2:     # news-api highlights
        generator = SearchGenerator()
        make_multiple_searches(generator.generate_searches(no_of_searches),
                               search_gap)