from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
from bs4 import BeautifulSoup as bs

# make chrome run in headless mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

# create a new instance of the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# set the maximum wait time for the driver to find an element
driver.implicitly_wait(10)

# navigate to the URL
url = 'https://scholar.google.com/citations?view_op=view_org&org=4770128543809686866&hl=en&oi=io'
driver.get(url)

user_links = []

while True:
    # parse the HTML with BeautifulSoup
    soup = bs(driver.page_source, 'html.parser')
    names = soup.find_all('h3', class_='gs_ai_name')
    for name in names:
        link = name.find('a')['href']
        if 'user' in link:
            if link not in user_links:
                # get the user link
                user_links.append(link)
                # get the name
                name_text = name.text.strip()
                print(link, name_text)
                # save the user link and name to a CSV file
                with open('googlescholars.csv', mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([link, name_text])

    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[aria-label="Next"]'))
    )
    next_button.click()

    # wait for a few seconds before proceeding to the next page
    time.sleep(2)

# close the browser window
driver.quit()