from selenium import webdriver
import os

url = 'https://www.youtube.com/kallehallden/videos'

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

browser = webdriver.Chrome(executable_path = DRIVER_BIN)
browser.get(url)

browser.find_element_by_xpath('//*[@id="thumbnail"]').click()