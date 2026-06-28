# kaggle_runner.py
from kaggle.api.kaggle_api_extended import KaggleApi

def trigger_kaggle():
    print("🚀 Triggering Kaggle Notebook via API...")
    try:
        api = KaggleApi()
        api.authenticate()
        
        print("Sending request to run the notebook...")
        
        # This is the correct way to run an existing notebook
        api.kernels_pull("dcfsvfdvbgb/updated-telebot-wan-vid", path=".", force=True)
        
        # Push a new version to trigger execution
        result = api.kernels_push("dcfsvfdvbgb/updated-telebot-wan-vid")
        
        print("✅ Kaggle Notebook triggered successfully!")
        return "✅ Success! Notebook is running on Kaggle."
        
    except Exception as e:
        print("Error:", str(e))
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    result = trigger_kaggle()
    print("FINAL RESULT:", result)