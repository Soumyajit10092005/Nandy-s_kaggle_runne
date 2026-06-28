from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import traceback

EMAIL = "Nandy-0050@proton.me"
PASSWORD = "Msfvenom123"
NOTEBOOK_URL = "https://www.kaggle.com/code/dcfsvfdvbgb/updated-telebot-wan-vid/edit"

def run_kaggle():
    print("🚀 Starting Kaggle Runner (Fast Mode)...")
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")

        service = Service("/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("Opening Kaggle...")
        driver.get(NOTEBOOK_URL)   # Directly go to notebook (if already logged in via profile)
        time.sleep(15)

        print("Trying to click Run All...")
        try:
            btn = driver.find_element("xpath", "//button[contains(text(), 'Run All')]")
            btn.click()
            print("✅ Run All clicked!")
            return "Success"
        except:
            print("Trying alternative selector...")
            btn = driver.find_element("xpath", "//button[contains(., 'Run')]")
            btn.click()
            print("✅ Run clicked!")
            return "Success"
        
    except Exception as e:
        print("Error:", traceback.format_exc())
        return f"Failed: {str(e)}"
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    result = run_kaggle()
    print("FINAL:", result)