# BLOXFRUITS BOT v2 — ONE FILE, ZERO SETUP
# Paste this into a new file: bot.py
# Run: python bot.py

import random, time, json, os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests

# ──────────────────────  YOUR SETTINGS  ──────────────────────
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1436382187854364722/O47XuHh1LuUa-mPOV4Ft41D6wHlWGRQTHu1athVx6dIqhuVcCJfw_7FMcx9NS-1EqMBA"
HOW_MANY_ACCOUNTS = 10
BASE_NAME = "BloxBot"
PASSWORD = "SuperSecure123!"
EMAIL_DOMAIN = "@tempmail.lol"   # works with 10minutemail, guerrillamail, etc.
# ─────────────────────────────────────────────────────────────

def notify(username, status, extra=""):
    color = 0x00ff00 if status == "CREATED" else 0xff0000
    requests.post(DISCORD_WEBHOOK, json={
        "embeds": [{
            "title": f"Account {status}",
            "description": f"**{username}**",
            "color": color,
            "fields": [
                {"name": "Password", "value": f"||{PASSWORD}||", "inline": True},
                {"name": "Email", "value": f"`{username.lower()}{EMAIL_DOMAIN}`", "inline": True},
                {"name": "Time", "value": datetime.now().strftime("%H:%M:%S"), "inline": True},
                {"name": "Details", "value": extra or "—"}
            ],
            "footer": {"text": "BloxFruits Bot • Hosted 24/7"}
        }]
    })

def create():
    username = f"{BASE_NAME}{random.randint(10000,99999)}"
    email = f"{username.lower()}{EMAIL_DOMAIN}"

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://www.roblox.com/")
        time.sleep(3)

        driver.find_element(By.ID, "signup-button").click()
        time.sleep(2)

        driver.find_element(By.ID, "signup-username").send_keys(username)
        driver.find_element(By.ID, "signup-password").send_keys(PASSWORD)
        driver.find_element(By.ID, "signup-email").send_keys(email)

        driver.execute_script('document.querySelector("#month").value = "1"')
        driver.execute_script('document.querySelector("#day").value = "1"')
        driver.execute_script('document.querySelector("#year").value = "2000"')

        print(f"\n[WAIT] Solve the CAPTCHA for **{username}** then press ENTER")
        input("   Press ENTER when you click SIGN UP...")

        time.sleep(6)
        success = "dashboard" in driver.current_url or "home" in driver.current_url

        if success:
            with open("accounts.txt", "a") as f:
                f.write(f"{username}:{PASSWORD}:{email}\n")
            notify(username, "CREATED", "Ready for BloxFruits auto-farm!")
            print(f"[SUCCESS] {username}")
        else:
            notify(username, "FAILED", "Probably CAPTCHA or rate-limit")
            print(f"[FAILED] {username}")

    except Exception as e:
        notify(username, "FAILED", str(e)[:100])
        print(f"[ERROR] {e}")
    finally:
        driver.quit()

# ──────────────────────  START BOT  ──────────────────────
if __name__ == "__main__":
    print("BloxFruits Account Factory STARTED")
    notify("BOT ONLINE", "CREATED", f"Will create {HOW_MANY_ACCOUNTS} accounts")
    
    for i in range(HOW_MANY_ACCOUNTS):
        create()
        time.sleep(15)  # Roblox loves slow humans

    notify("BOT FINISHED", "CREATED", "All done! Check accounts.txt")
    print("\nAll done! Accounts saved to accounts.txt")
