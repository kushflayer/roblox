# account_creator.py
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import *
from webhook import send  # ← NEW

# ←←←  ADD YOUR WEBHOOK URL HERE  ←←←
WEBHOOK_URL = "https://discord.com/api/webhooks/..."   # ← PUT YOUR URL

def create_account(username, password, email):
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # remove if you want to see browser
    driver = webdriver.Chrome(service=service, options=options)
    
    success = False
    details = ""
    
    try:
        driver.get("https://www.roblox.com/signup")
        time.sleep(3)

        driver.find_element(By.ID, "signup-username").send_keys(username)
        driver.find_element(By.ID, "signup-password").send_keys(password)
        driver.find_element(By.ID, "signup-email").send_keys(email)

        # Birthday
        driver.find_element(By.ID, "month").send_keys(BIRTH_MONTH)
        driver.find_element(By.ID, "day").send_keys(BIRTH_DAY)
        driver.find_element(By.ID, "year").send_keys(BIRTH_YEAR)

        print(f"[+] {username} → Solve CAPTCHA, then press ENTER")
        input("    Press ENTER after you submit...")

        time.sleep(6)
        if "create" in driver.current_url.lower() or "dashboard" in driver.current_url.lower():
            success = True
            details = f"Email: {email}"
            with open("created_accounts.txt", "a") as f:
                f.write(f"{username}:{password}:{email}\n")
        else:
            details = driver.page_source[:200]

    except Exception as e:
        details = str(e)[:200]
    finally:
        driver.quit()

    # ←←←  SEND RESULT TO YOUR HOSTING  ←←←
    send(WEBHOOK_URL, username, "SUCCESS" if success else "FAILED", details)
    print(f"{'SUCCESS' if success else 'FAILED'} → {username}")

if __name__ == "__main__":
    for i in range(NUM_ACCOUNTS):
        username = f"{BASE_USERNAME}{random.randint(1000,99999)}"
        email = f"{username.lower()}{EMAIL_DOMAIN}"
        create_account(username, PASSWORD, email)
        time.sleep(12)  # anti-rate-limit
