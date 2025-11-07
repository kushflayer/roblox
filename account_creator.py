import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import NUM_ACCOUNTS, BASE_USERNAME, PASSWORD, BIRTH_MONTH, BIRTH_DAY, BIRTH_YEAR, EMAIL_DOMAIN

def create_account(username, password, email):
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Go to Roblox signup
        driver.get("https://www.roblox.com/signup")
        time.sleep(2)
        
        # Fill username
        username_field = driver.find_element(By.ID, "signup-username-field")
        username_field.send_keys(username)
        
        # Fill password
        password_field = driver.find_element(By.ID, "signup-password-field")
        password_field.send_keys(password)
        
        # Fill email (generate temp email)
        email_field = driver.find_element(By.ID, "signup-email-field")
        email_field.send_keys(email)
        
        # Gender (select first option)
        gender_select = driver.find_element(By.ID, "signup-gender")
        gender_select.click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//option[@value='Male']").click()  # Or 'Female'
        
        # Birthday
        month_select = driver.find_element(By.ID, "month")
        month_select.send_keys(BIRTH_MONTH)
        day_select = driver.find_element(By.ID, "day")
        day_select.send_keys(BIRTH_DAY)
        year_select = driver.find_element(By.ID, "year")
        year_select.send_keys(BIRTH_YEAR)
        
        # Submit (but pause for CAPTCHA)
        print(f"Account {username}: Form filled. Solve CAPTCHA manually in browser, then press Enter here.")
        input("Press Enter after solving CAPTCHA and submitting...")
        
        # Wait for success (check for dashboard or error)
        time.sleep(5)
        if "dashboard" in driver.current_url.lower():
            print(f"Success: {username} created!")
            with open("created_accounts.txt", "a") as f:
                f.write(f"{username}:{password}:{email}\n")
        else:
            print(f"Failed: {username}")
            
    except Exception as e:
        print(f"Error for {username}: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    for i in range(NUM_ACCOUNTS):
        username = f"{BASE_USERNAME}{random.randint(1000, 9999)}"
        email = f"{username.lower()}{EMAIL_DOMAIN}"
        create_account(username, PASSWORD, email)
        time.sleep(10)  # Delay to avoid rate limits
