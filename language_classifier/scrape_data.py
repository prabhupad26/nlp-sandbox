"""
TODO: Scrape the data from https://tatoeba.org/eng/
Get the data in a csv file in below format

1, en, The weather is nice today.
1, de, Das Wetter ist heute schön.
1, es, El clima es agradable hoy.
1, el, Ο καιρός είναι καλός σήμερα.
...

"""
import requests
from selenium import webdriver
import chromedriver_autoinstaller


def start_scraping(driver):
    final_dictionary = []
    index = 0
    while len(final_dictionary) != 10000:
        driver.get("https://tatoeba.org/eng/sentences/show/random")
        index += 1

if __name__ == '__main__':
    print("Running unittest for validating selenium webdriver")
    chromedriver_autoinstaller.install()
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--remote-debugging-port=9222")
    chromeOptions.add_argument("--headless")
    # chromeOptions.add_argument("--no-sandbox")
    # chromeOptions.add_argument("--disable-setuid-sandbox")
    # chromeOptions.add_argument("--disable-dev-shm-using")
    # chromeOptions.add_argument("--disable-extensions")
    # chromeOptions.add_argument("--disable-gpu")
    # chromeOptions.add_argument("start-maximized")
    # chromeOptions.add_argument("disable-infobars")
    driver = webdriver.Chrome(options=chromeOptions)
    try:
        driver.get("http://www.python.org")
        assert "Python" in driver.title
    except Exception as e:
        print(f"Error occured : {e}")
    finally:
        driver.close()