import telebot
import subprocess
import threading
import os
import time

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

is_running = False
current_process = None

def run_kaggle_task(chat_id):
    global is_running, current_process
    is_running = True
    
    try:
        bot.send_message(chat_id, "🚀 **Starting Kaggle Notebook**\nPlease wait, this may take 30-60 seconds...")
        
        current_process = subprocess.Popen(
            ["python", "kaggle_runner.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        stdout, stderr = current_process.communicate(timeout=240)
        
        output = stdout.strip() or stderr.strip() or "No output received."
        bot.send_message(chat_id, f"✅ **Execution Finished**\n\n{output}")
        
    except subprocess.TimeoutExpired:
        bot.send_message(chat_id, "⏰ **Timeout**: Operation took too long.")
        if current_process:
            current_process.kill()
    except Exception as e:
        bot.send_message(chat_id, f"❌ **Error**: {e}")
    finally:
        is_running = False
        current_process = None

@bot.message_handler(commands=['run'])
def handle_run(message):
    global is_running
    if is_running:
        bot.reply_to(message, "⚠️ A task is already running. Use /status to check.")
        return
    
    thread = threading.Thread(target=run_kaggle_task, args=(message.chat.id,))
    thread.daemon = True
    thread.start()

@bot.message_handler(commands=['status'])
def handle_status(message):
    if is_running:
        bot.reply_to(message, "🔄 **Status**: Kaggle notebook is currently **RUNNING**...")
    else:
        bot.reply_to(message, "⭕ **Status**: No task is running.\nSend /run to start.")

@bot.message_handler(commands=['end', 'stop'])
def handle_stop(message):
    global is_running, current_process
    if is_running and current_process:
        try:
            current_process.kill()
            bot.reply_to(message, "🛑 **Stopped** current execution.")
        except:
            bot.reply_to(message, "⚠️ Could not stop the process.")
    else:
        bot.reply_to(message, "✅ No running task to stop.")
    is_running = False

@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.reply_to(message, 
        "🤖 **Kaggle Runner Bot**\n\n"
        "Available Commands:\n"
        "/run    → Start Kaggle Notebook\n"
        "/status → Check current status\n"
        "/end    → Stop current execution\n"
        "/help   → Show this message")

print("🤖 Bot started successfully...")
bot.infinity_polling()