from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = Options()
#options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="/Users/christiangrinling/Desktop/chromedriver2",options=options)

sneakerurl = 'https://www.checkcardetails.co.uk/'

driver.get(sneakerurl)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

results = soup.find(id='maincontent')
print(results)
time.sleep(5)
driver.quit()
