# kaggle_runner.py
import os
from kaggle.api.kaggle_api_extended import KaggleApi
import time
# this is nprw
def trigger_kaggle():
    print("🚀 Triggering Kaggle Notebook via API...")
    try:
        api = KaggleApi()
        api.authenticate()
        
        # Your notebook details
        owner_slug = "dcfsvfdvbgb"
        kernel_slug = "updated-telebot-wan-vid"
        
        print(f"Pushing version to {owner_slug}/{kernel_slug}...")
        
        result = api.kernels_push(
            kernel_slug=kernel_slug,
            new_title="Auto Triggered - Telebot Wan Vid",
            version_type="save_version",
            is_private=False
        )
        
        print("✅ Kaggle Notebook started successfully!")
        return "Kaggle Notebook Triggered via API!"
        
    except Exception as e:
        print("Error:", e)
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    result = trigger_kaggle()
    print("FINAL RESULT:", result)