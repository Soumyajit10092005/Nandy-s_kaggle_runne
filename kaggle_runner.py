from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import traceback

EMAIL = "Nandy-0050@proton.me"
PASSWORD = "Msfvenom123"
NOTEBOOK_URL = "https://www.kaggle.com/code/dcfsvfdvbgb/updated-telebot-wan-vid/edit"

def run_kaggle():
    print("🚀 Starting Kaggle Runner (webdriver-manager mode)...")
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        print("✅ Chrome Driver Started")
        
        print("Opening Notebook directly...")
        driver.get(NOTEBOOK_URL)
        time.sleep(15)

        print("Trying to click Run All...")
        try:
            btn = driver.find_element("xpath", "//button[contains(text(), 'Run All')]")
            btn.click()
            print("✅ Run All clicked successfully!")
            return "Success"
        except Exception as e:
            print("Run All button not found:", e)
            return "Button not found"
        
    except Exception as e:
        print(traceback.format_exc())
        return f"Failed: {str(e)}"
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    result = run_kaggle()
    print("FINAL RESULT:", result)