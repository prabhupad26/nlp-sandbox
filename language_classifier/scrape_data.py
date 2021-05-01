import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


def start_scraping(driver_obj):
    final_dictionary = []
    index = 1
    while len(final_dictionary) != 1000:
        print(f"Processed {len(final_dictionary)}")
        temp_num = 1
        temp_div_pos = 0
        temp_div_pos2 = 0
        temp_span = '/span'
        value_dict = {}
        driver_obj.get("https://tatoeba.org/eng/sentences/show/random")
        print(f"Currently fetching from : {driver_obj.current_url}")
        time.sleep(2)
        try:
            expand_show_more = driver_obj.find_element_by_xpath("/html/body/div[3]/div/div[3]/section[1]/"
                                                                "div/div[4]/button")
            expand_show_more.click()
        except NoSuchElementException:
            print("show more link is not there")
        for dom_index in range(1, 6):
            try:
                print(f"Fetching #{dom_index} position")
                if dom_index >= 3:
                    temp_div_pos2 += 1
                xpath_base_lang = f"/html/body/div[3]/div/div[3]/section[1]/div" \
                                  f"/div[{1 + temp_div_pos}]/div[{2 + temp_div_pos2}]/div/div/div[{temp_num}]/language-icon/img"
                xpath_base_text = f"/html/body/div[3]/div/div[3]/section[1]/div" \
                                  f"/div[{1 + temp_div_pos}]/div[{2 + temp_div_pos2}]/div/div/div[{temp_num + 1}]/span{temp_span}"
                lang = driver_obj.find_element_by_xpath(xpath_base_lang).get_attribute('title')
                text = driver_obj.find_element_by_xpath(xpath_base_text).text
                value_dict[lang] = text
                if temp_num == 1:
                    # Needs to be updated only one time
                    temp_num += 1
                    temp_div_pos += 1
                    temp_span = ''
                print(f"Fetching #{dom_index} position success")
            except NoSuchElementException:
                value_dict['error'] = f'Not enough sentences in {driver_obj.current_url}'
        final_dictionary.append(value_dict)
        index += 1
    df = pd.DataFrame(columns=['id', 'language', 'sentence'])
    _id = 1
    for i in final_dictionary:
        for lang in i:
            df = df.append({'id': _id, 'language': lang, 'sentence': i[lang]}, True)
        _id += 1
    df.to_csv('data/language_data.csv', index=False)


if __name__ == '__main__':
    print("Running unittest for validating selenium webdriver")
    chromedriver_autoinstaller.install()
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless")
    # chromeOptions.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chromeOptions)
    try:
        driver.get("http://www.python.org")
        assert "Python" in driver.title
        # start_scraping(driver)
    except Exception as e:
        print(f"Error occurred : {e}")
    finally:
        driver.close()
