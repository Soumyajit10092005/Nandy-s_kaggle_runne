# kaggle_runner.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import traceback

EMAIL = "Nandy-0050@proton.me"
PASSWORD = "Msfvenom123"
NOTEBOOK_URL = "https://www.kaggle.com/code/dcfsvfdvbgb/updated-telebot-wan-vid/edit"

def run_kaggle():
    print("🚀 Starting Kaggle Runner (Debug Mode)...")
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        
        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        wait = WebDriverWait(driver, 40)  # Increased timeout
        
        print("1. Opening Kaggle Login...")
        driver.get("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F")
        time.sleep(10)   # Extra wait for full load
        
        print("2. Looking for Email Field...")
        email_selectors = [
            (By.CSS_SELECTOR, "input[type='email']"),
            (By.NAME, "email"),
            (By.XPATH, "//input[contains(@placeholder, 'email')]")
        ]
        
        email_field = None
        for by, sel in email_selectors:
            try:
                email_field = wait.until(EC.presence_of_element_located((by, sel)))
                print(f"✅ Found email field with: {sel}")
                break
            except:
                continue
        
        if not email_field:
            print("❌ Could not find email field. Current page title:", driver.title)
            print("Page source snippet:", driver.page_source[:500])
            return "Failed to find login form"
        
        email_field.clear()
        email_field.send_keys(EMAIL)
        time.sleep(3)

        print("3. Entering Password...")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_field.send_keys(PASSWORD)
        time.sleep(3)

        print("4. Clicking Sign In...")
        signin_btn = driver.find_element(By.XPATH, "//button[contains(., 'Sign in') or @type='submit']")
        signin_btn.click()
        time.sleep(15)

        print("5. Opening Notebook...")
        driver.get(NOTEBOOK_URL)
        time.sleep(12)

        print("6. Clicking Run All...")
        run_selectors = [
            (By.XPATH, "//button[contains(text(), 'Run All')]"),
            (By.XPATH, "//button[contains(text(), 'Run all')]"),
        ]
        
        clicked = False
        for by, sel in run_selectors:
            try:
                btn = wait.until(EC.element_to_be_clickable((by, sel)))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(2)
                btn.click()
                print("✅ SUCCESS: Run All clicked!")
                clicked = True
                break
            except:
                continue
        
        if not clicked:
            print("❌ Run All button not found.")
        
        return "Kaggle Notebook Triggered!"
        
    except Exception as e:
        error = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error)
        return error
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    result = run_kaggle()
    print("FINAL RESULT:", result)