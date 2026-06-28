# kaggle_runner.py
from kaggle.api.kaggle_api_extended import KaggleApi
import time

def trigger_kaggle():
    print("🚀 Triggering Kaggle Notebook via API...")
    try:
        api = KaggleApi()
        api.authenticate()
        
        print("Pushing new version to run the notebook...")
        
        # This will create a new version and run it
        result = api.kernels_push(
            "dcfsvfdvbgb/updated-telebot-wan-vid",   # Full slug
            version_type="save_version"
        )
        
        print("✅ Kaggle Notebook triggered successfully!")
        return "✅ Kaggle Notebook Started Successfully!"
        
    except Exception as e:
        print("Error:", str(e))
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    result = trigger_kaggle()
    print("FINAL RESULT:", result)