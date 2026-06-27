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
    print("🚀 Starting Kaggle Runner...")
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=Service(), options=chrome_options)
        wait = WebDriverWait(driver, 30)
        
        print("1. Opening Kaggle Login Page...")
        driver.get("https://www.kaggle.com/account/login?phase=emailSignIn&returnUrl=%2F")
        time.sleep(8)

        print("2. Entering Email...")
        email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='email']")))
        email_field.send_keys(EMAIL)
        time.sleep(2)

        print("3. Entering Password...")
        password_field = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_field.send_keys(PASSWORD)
        time.sleep(2)

        print("4. Clicking Sign In...")
        signin_btn = driver.find_element(By.XPATH, "//button[contains(., 'Sign in') or @type='submit']")
        signin_btn.click()
        time.sleep(12)

        print("5. Opening Notebook...")
        driver.get(NOTEBOOK_URL)
        time.sleep(10)

        print("6. Looking for 'Run All' button...")
        found = False
        selectors = [
            "//button[contains(text(), 'Run All')]",
            "//button[contains(text(), 'Run all')]",
            "//*[contains(text(), 'Run All')]/ancestor::button"
        ]
        
        for sel in selectors:
            try:
                btn = wait.until(EC.element_to_be_clickable((By.XPATH, sel)))
                print(f"Found button with selector: {sel}")
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn)
                time.sleep(2)
                btn.click()
                print("✅ SUCCESS: Run All button clicked!")
                found = True
                break
            except Exception as e:
                print(f"Selector failed: {sel} | Error: {e}")
                continue
        
        if not found:
            print("❌ Could not find Run All button.")
            print("Current page title:", driver.title)
            
        return "Kaggle Run Triggered Successfully!"
        
    except Exception as e:
        error_msg = f"Error: {str(e)}\n{traceback.format_exc()}"
        print(error_msg)
        return error_msg
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    result = run_kaggle()
    print("Final Result:", result)