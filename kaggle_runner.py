# kaggle_runner.py
from kaggle.api.kaggle_api_extended import KaggleApi

def trigger_kaggle():
    print("🚀 Triggering Kaggle Notebook via API...")
    try:
        api = KaggleApi()
        api.authenticate()
        
        print("Pushing new version to start the notebook...")
        
        # Pass the path to the LOCAL folder containing kernel-metadata.json
        # Use "." if the metadata file is in the exact same directory as this script
        local_folder_path = "./my_kaggle_notebook" 
        
        result = api.kernels_push(local_folder_path)
        
        print("✅ Kaggle Notebook triggered successfully!")
        return "✅ Success! Notebook is running on Kaggle."
        
    except Exception as e:
        print("Error:", str(e))
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    result = trigger_kaggle()
    print("FINAL RESULT:", result)