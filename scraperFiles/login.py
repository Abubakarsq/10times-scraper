import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://10times.com/events"


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email):
        self.driver.get(URL)
        self.driver.find_element(By.ID, "loginHide").click()
        self.driver.implicitly_wait(5)
        email_field = self.driver.find_element(By.ID, "valEmail")
        email_field.clear()
        email_field.send_keys(email)
        email_field.send_keys(Keys.ENTER)
        self.input_otp()

    def input_otp(self):
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "input.text-blue").click()
        print("waiting for otp ....")
        otp = input("please enter the otp you received:\t")
        otp_field = self.driver.find_element(By.CSS_SELECTOR, "input[name='OTP']")
        otp_field.click()
        otp_field.send_keys(otp)
        otp_field.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.get("https://10times.com/events")
        print("-------- successfully logged in --------")
