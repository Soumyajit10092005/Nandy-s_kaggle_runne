import os
import json
from kaggle.api.kaggle_api_extended import KaggleApi

def trigger_kaggle():
    print("🚀 Triggering Kaggle Notebook via API...")
    try:
        # 1. Define folder path and check for your notebook file
        folder_path = "./my_kaggle_notebook"
        notebook_filename = "updated_telebot_wan_vid.ipynb"
        
        # Target path where Kaggle API expects the notebook
        target_notebook_path = os.path.join(folder_path, notebook_filename)
        metadata_path = os.path.join(folder_path, "kernel-metadata.json")
        
        # Ensure the push directory exists
        os.makedirs(folder_path, exist_ok=True)
        
        # 2. Find where your notebook actually is and copy/create it in the folder
        if os.path.exists(notebook_filename):
            # If notebook is in the root directory, read it
            with open(notebook_filename, 'r', encoding='utf-8') as f:
                notebook_content = json.load(f)
        elif os.path.exists(target_notebook_path):
            # If it's already in the subfolder, read it
            with open(target_notebook_path, 'r', encoding='utf-8') as f:
                notebook_content = json.load(f)
        else:
            # Fallback: Create a lightweight boilerplate notebook if not found anywhere
            print("⚠️ Notebook file not found locally. Generating a placeholder notebook.")
            notebook_content = {
                "cells": [{"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["# Automatically triggered via Render API"]}],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 2
            }

        # Write the notebook into the target push folder
        with open(target_notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook_content, f)
        
        # 3. Dynamically generate the metadata JSON
        metadata = {
            "id": "dcfsvfdvbgb/updated-telebot-wan-vid",
            "title": "updated-telebot-wan-vid",
            "code_file": notebook_filename,
            "language": "python",
            "kernel_type": "notebook",
            "is_private": "true",
            "enable_gpu": "true",
            "enable_tpu": "false",
            "enable_internet": "true",
            "dataset_sources": [],
            "competition_sources": [],
            "kernel_sources": []
        }
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f)

        # 4. Authenticate and Push via Kaggle API
        api = KaggleApi()
        api.authenticate()
        
        print("Pushing new version to start the notebook...")
        result = api.kernels_push(folder_path)
        
        print("✅ Kaggle Notebook triggered successfully!")
        return "✅ Success! Notebook is running on Kaggle."
        
    except Exception as e:
        print("Error:", str(e))
        return f"Failed: {str(e)}"

if __name__ == "__main__":
    result = trigger_kaggle()
    print("FINAL RESULT:", result)