import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def loginInput(input):
    loginBox.clear()
    loginBox.send_keys(input)

def passwordInput(input):
    passwordBox.clear()
    passwordBox.send_keys(input)

dictLoginPassword = {
    "" :                        ["secret_sauce", "", "wrong_password"],
    "standard_user" :           ["secret_sauce", "", "wrong_password", "standard_user"],
    "locked_out_user" :         ["secret_sauce", "", "wrong_password", "locked_out_user"],
    "problem_user" :            ["secret_sauce", "", "wrong_password", "problem_user"],
    "performance_glitch_user" : ["secret_sauce", "", "wrong_password", "performance_glitch_user"],
    "error_user" :              ["secret_sauce", "", "wrong_password", "error_user"],
    "visual_user" :             ["secret_sauce", "", "wrong_password", "visual_user"],
    "secret_sauce" :            ["secret_sauce", "", "wrong_password"]
}

driver = webdriver.Firefox()
website = "https://www.saucedemo.com/"

driver.get(website)
print(driver.title)
print()

loginBox = driver.find_element(By.ID, "user-name")
passwordBox = driver.find_element(By.ID, "password")
loginBtn = driver.find_element(By.ID, "login-button")

print("testing login/password for different users")

for key in dictLoginPassword:
    loginInput(key)
    for password in dictLoginPassword[key]:
        passwordInput(password)
        loginBtn.send_keys(Keys.ENTER)
        if (driver.current_url == "https://www.saucedemo.com/inventory.html"):
            print("Testing login \"{}\" with password \"{}\" succeed".format(key, password))
            driver.back()
            loginBox = driver.find_element(By.ID, "user-name")
            passwordBox = driver.find_element(By.ID, "password")
            loginBtn = driver.find_element(By.ID, "login-button")
        else:
            print("Testing login \"{}\" with password \"{}\" failed".format(key, password))
    print()

#wait until element fully loaded or 2 sec
#elem = WebDriverWait(driver, 2).until(EC.visibilityOfAllElements())

driver.quit()