import os
import telethon
from telethon import TelegramClient
from services.openai_service import get_openai_response
import json

# File to store user-specific configurations
CONFIG_FILE = "user_config.json"

def prompt_for_openai_key():
    """
    Prompt the user for their OpenAI API key and save it securely for this session.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        if "openai_api_key" in config:
            return config["openai_api_key"]
    
    openai_key = input("Enter your OpenAI API key: ").strip()
    save_openai_key(openai_key)
    return openai_key

def save_openai_key(openai_key):
    """
    Save the OpenAI API key to a local configuration file.
    """
    config = {}
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
    config["openai_api_key"] = openai_key
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)

def load_openai_key():
    """
    Load the OpenAI API key from the configuration file.
    """
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            config = json.load(file)
        return config.get("openai_api_key")
    return None

def main():
    print("Starting user setup...")
    openai_key = prompt_for_openai_key()

    # Initialize Telethon client
    print("Starting Telegram bot...")
    api_id = 24785086  # Replace with your API ID
    api_hash = "139c9b15b0352f21de41cdf693bba53c"  # Replace with your API hash
    client = TelegramClient("my_userbot", api_id, api_hash)

    # Define Telegram message handler
    @client.on(telethon.events.NewMessage)
    async def handler(event):
        user_message = event.message.message
        response = get_openai_response(user_message, openai_key)
        await event.reply(response)

    # Start Telegram bot
    print("Bot is running...")
    client.start()
    client.run_until_disconnected()

if __name__ == "__main__":
    main()
