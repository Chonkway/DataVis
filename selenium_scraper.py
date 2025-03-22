# import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import os, json

"""
Executing this script will update ALL DATA within the DATA directory by scraping the WHO site for all country health data.

Don't execute this frequently...
"""

#Interact with a link if it exists and matches a country name. Save to a defined data directory
def country_content (cname: str):
    try:
        cont_link = driver.find_element(By.LINK_TEXT, cname)
        cont_link.click()

        data_set_link  = driver.find_element(By.XPATH, "//span[text()='Download Dataset Package']")
        data_set_link.click()

    except NoSuchElementException:
        print(cname + "Not Found!")
        pass



#Def dir for datasets
download_path = "C:\\Users\\Sable\\PyCharmMiscProject\\data"
os.makedirs(os.path.dirname(download_path), exist_ok=True)
country_list= './Content/country_list.json'

# create webdriver object, pass new profile overrides
options = Options()
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", download_path)
service = webdriver.FirefoxService()
driver = webdriver.Firefox(options=options, service=service)



# get the WHO country data page
driver.get("https://data.who.int/countries")
driver.maximize_window()

#country_content('Cambodia')

#Open country list json and step through all names
with (open("C:\\Users\\Sable\\PyCharmMiscProject\\Content\\country_list.json", 'r') as file):
    content = json.load(file)

    for item in content:
        country_name = item["name"]
        #print(country_name)
        country_content(country_name)
        driver.back()

print("All Done <3")
driver.close()
