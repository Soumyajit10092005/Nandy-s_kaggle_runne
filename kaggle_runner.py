# kaggle_runner.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

EMAIL = "Nandy-0050@proton.me"
PASSWORD = "Msfvenom123"
NOTEBOOK_URL = "https://www.kaggle.com/code/dcfsvfdvbgb/updated-telebot-wan-vid/edit"

def run_kaggle():
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        wait = WebDriverWait(driver, 25)
        
        print("🔐 Logging into Kaggle...")
        driver.get("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F")
        time.sleep(7)

        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']"))).send_keys(EMAIL)
        time.sleep(2)
        
        driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(PASSWORD)
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//button[contains(., 'Sign in') or @type='submit']").click()
        time.sleep(12)

        print("📂 Opening Notebook...")
        driver.get(NOTEBOOK_URL)
        time.sleep(12)

        print("▶️ Clicking Run All...")
        selectors = [
            "//button[contains(text(), 'Run All')]",
            "//button[contains(text(), 'Run all')]",
            "//*[contains(text(), 'Run All')]/ancestor::button"
        ]
        
        for sel in selectors:
            try:
                btn = wait.until(EC.element_to_be_clickable((By.XPATH, sel)))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(2)
                btn.click()
                print("✅ SUCCESS: Run All executed!")
                return "✅ Kaggle notebook started successfully!"
            except:
                continue
                
        return "⚠️ Could not find Run All button."
        
    except Exception as e:
        return f"❌ Error: {str(e)}"
    finally:
        if driver:
            driver.quit()