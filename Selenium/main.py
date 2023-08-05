from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

#Chose driver to browse
options = Options()
options.add_argument("executable_path=/home/garga/Projects/Python/LinkedInBot/geckodriver")

driver = webdriver.Firefox(options=options)
#options=options, executable_path='/home/garga/Projects/Python/LinkedInBot/geckodriver'

#Open website
driver.get("https://br.linkedin.com/")
sleep(2)

#Confirm Title
#assert "LinkedIn" in driver.title

#Wait login by user (input email and password, click login button and set "enter" in terminal)
print(f'\n\nSeu login deve ser feito manualmente. Assim que logar, tecle ENTER.\n\n')
input()
sleep(4)

#Find element and click
elem = driver.find_element(By.XPATH, '/html/body/div[5]/header/div/nav/ul/li[2]')
elem.click()

#Wait 4 seconds and scroll page
sleep(4)
driver.execute_script("window.scrollTo(0, 2300);")

#Wait 2 seconds and repeatedly click the "connect" button
sleep(2)

while(True):
    elem = driver.find_element(By.XPATH, "/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/ul/li[1]/ul/li[1]/div/section/div[3]/footer/button/span")
    elem.click()
    sleep(1)
    try:
        elem = driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div[3]/button[1]/span")
        elem.click()
        sleep(1)
    except:
        None        
