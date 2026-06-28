# kaggle_runner.py
from kaggle.api.kaggle_api_extended import KaggleApi

def trigger_kaggle():
    print("🚀 Triggering Kaggle Notebook via API...")
    try:
        api = KaggleApi()
        api.authenticate()
        
        print("Pushing new version...")
        
        # Correct way
        result = api.kernels_push("dcfsvfdvbgb/updated-telebot-wan-vid")
        
        print("✅ Kaggle Notebook triggered successfully!")
        return "✅ Success! Notebook is running on Kaggle."
        
    except Exception as e:
        print("Error:", str(e))
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    result = trigger_kaggle()
    print("FINAL RESULT:", result)