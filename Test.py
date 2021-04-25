from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
driver = webdriver.Chrome(r"/usr/lib/chromium-browser/chromedriver",options=chrome_options)
driver.get('https://chartink.com/screener/meanreversionstrategy')

# click Excel button to download the file
python_button = driver.find_element_by_css_selector('.btn.btn-default.buttons-excel.buttons-html5.btn-primary')
python_button.click()