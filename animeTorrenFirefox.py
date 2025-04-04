from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import re,os

def init_driver():
    option=Options()
    option.add_argument("--width=800") 
    option.add_argument("--height=800") 
    option.add_argument("--headless")
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=option)
    driver.get("https://www.nyaa.si")
    return driver
 
def searchAnime(Anime,Category):
    driver=init_driver()
    #driver=headlessInitVar()
    #wait_for_page_load(driver)
    driver.implicitly_wait(10)

    links=driver.find_element("xpath","//button[@class='navbar-toggle collapsed']")
    links.click()
    links=driver.find_element("xpath","//*[@name='q']")
    links.click()
    links.send_keys(Anime)
    #select category by Category variable
    dropdown = Select(driver.find_element(By.NAME, "c"))
    dropdown.select_by_visible_text(Category)
    #old method single category only   
    #links=driver.find_element("xpath","//*[@title='Category']")
    #links.click()
    #links=driver.find_element("xpath","//*[@title='Anime']")
    #links.click()
    links=driver.find_element("xpath","//button[@class='btn btn-primary form-control']")
    links.click()
    driver.implicitly_wait(10)
    #find entries with green background
    list=driver.find_elements(By.XPATH,"//tbody//tr[@class='success']//td[@colspan='2']//a")
    count=-2
    for lists in list:
        print(lists.text)
        count+=1
    #end Selenium Driver    
    print("Found ",count)
    confirm =input("Proceed to download torrent/s ? Y/N     ")
    if confirm.upper() == 'Y':
        link= driver.find_elements(By.XPATH,"//tbody//tr[@class='success']//td[@class='text-center']//a//i[@class='fa fa-fw fa-download']")
        for links in link:
            links.click()       
        driver.implicitly_wait(20)
        print("Torrent Downloaded!")
        driver.quit()
    else:
        driver.quit()
    #
    #if a complete anime episodes are existing download it first

def extract_range_pattern(input_string):
    # Regular expression pattern to match "1-12", "1-99", etc.
    pattern = r'\b\d+\s*[-~]\s*\d+\b'
    
    # Search for the pattern in the input string
    match = re.search(pattern, input_string)
    
    # If a match is found, return it
    if match:
        return match.group()
    else:
        return None



os.system('cls')
#type anime title here!
name = input("Enter Anime/Manga Title here! \n")
cat= input("Enter search Category: (Anime, Literature) \n")
searchAnime(name,cat)
exit()
