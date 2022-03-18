from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import json

class InstagramBot:
    def __init__(self):
        options = Options()
        options.binary_location="*PATH TO FIREFOX*"
        self.driver = webdriver.Firefox(executable_path="*PATH TO GECKODRIVER*", options=options) 
        self.count=0
        self.user = self.read_json()

    def click_element(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        element.click()

        return element

    def manual_input(self, message):
        print(message)
        return str(input())

    def login(self):
        try:
            #GO TO INSTAGRAM
            self.driver.get("https://www.instagram.com/")

            ################# INPUT DATA #################
            #EMAIL FIELD
            email = self.manual_input("Enter the username, phone number, or email:")
            element = self.click_element("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
            element.clear()
            element.send_keys(email)
            sleep(2)

            #PASSWORD FIELD
            password = self.manual_input("Enter the password:")
            element = self.click_element("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
            element.clear()
            element.send_keys(password)
            sleep(2)

            #CLICK IN BUTTON LOGIN
            element = self.click_element("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
            sleep(5)

            ################# IF NOT WORKING #################
            try:
                self.driver.find_element(By.XPATH, "//*[@id='slfErrorAlert']")
                print("The username or password does not match!")
                self.driver.refresh()
                sleep(3)
                self.login()
            except:
                self.click_element("/html/body/div[1]/section/main/div/div/div/div/button")
                sleep(3)
                self.click_element("/html/body/div[6]/div/div/div/div[3]/button[2]")
        except:
            sleep(3)
            self.login()

    def find_account(self):
        ################# FIND USER #################
        try:
            try:
                #SELECT DIV ABOVE
                self.click_element("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[1]/div")
                sleep(1)
            except:
                pass

            #SELECT DIV BELOW
            element = self.click_element("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input")
            sleep(1)

            #ENTER USERNAME
            element.clear()
            print(f'\n\n{self.user[self.count]}\n\n')
            element.send_keys(str(self.user[self.count]))
            self.count+=1
            sleep(1)

            #SELECT DIV
            element = self.click_element("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div/a/div/div[2]/div[1]/div/div")
            sleep(2)
        except:
            sleep(2)
            self.driver.get("https://www.instagram.com/")
            sleep(2)
            self.find_account()

    def follow(self):
        try:
            #SEND MESSAGE
            self.driver.find_element(By.XPATH, "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button/div/div/span")
            #self.send_message()
        except:
            #FOLLOW
            self.click_element("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button/div")
            sleep(1)
            #self.send_message()

    def send_message(self):
        #CLICK IN MESSAGE BUTTON
        self.click_element("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/button/div")
        sleep(2)

        #CLICK IN MESSAGE FIELD
        element = self.click_element("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
        element.clear()
        sleep(2)

        #INPUT TEXT
        element.send_keys("Olá, Gabriel! Vim por meio do seu bot do Instagram...")

    def read_json(self):
        with open('users.json') as file:
            data = json.load(file)
            user = []
            for i in range(0, len(data)):
                user.append(data[i]['username'])
            file.close()
        return user

#DEFINE BOT
bot = InstagramBot()

#SIGN IN
bot.login()        

for i in range(0,2): #2 -> NUMBER OF ACCOUNTS
    #FIND ACCOUNT
    bot.find_account()

    #FOLLOW
    bot.follow()