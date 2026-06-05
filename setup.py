import asyncio
import os
import sys

from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.errors import ApiIdInvalidError


ENV_FILE = ".env"
SESSION_FILE = "my_session.session"


# -------- Create .env file from user input --------
def create_env_file():
    print("\n📋 No .env file found. Let's set it up.")
    print("You can get your API credentials from: https://my.telegram.org/apps\n")

    while True:
        api_id = input("Enter your App api_id: ").strip()
        if api_id.isdigit():
            break
        print("❌ api_id must be a number. Try again.")

    api_hash = input("Enter your App api_hash: ").strip()
    if not api_hash:
        print("❌ api_hash cannot be empty.")
        sys.exit(1)

    with open(ENV_FILE, "w") as f:
        f.write(f"API_ID={api_id}\n")
        f.write(f"API_HASH={api_hash}\n")

    print(f"\n✅ .env file created successfully.\n")


# -------- Login and create session --------
async def create_session():
    load_dotenv()
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")

    if not api_id or not api_hash:
        print("❌ Could not read API credentials from .env file.")
        sys.exit(1)

    print("\n🔐 Starting Telegram login to create your session...")
    try:
        client = TelegramClient("my_session", int(api_id), api_hash)
        await client.start()
        me = await client.get_me()
        print(f"\n✅ Logged in successfully as: {me.first_name} (@{me.username})")
        await client.disconnect()

    except ApiIdInvalidError:
        print("\n❌ Invalid API credentials. Please check your api_id and api_hash.")
        # Remove invalid .env so user can re-run setup
        if os.path.exists(ENV_FILE):
            os.remove(ENV_FILE)
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Login failed: {e}")
        sys.exit(1)


# -------- Main setup flow --------
async def run_setup():
    # Step 1: Create .env if missing
    if not os.path.exists(ENV_FILE):
        create_env_file()
    else:
        print("✅ .env file already exists.")

    # Step 2: Skip session creation if session already exists
    if os.path.exists(SESSION_FILE):
        print("✅ Session file already exists. Skipping login.")
        return

    # Step 3: Ask user before logging in
    answer = input("\nDo you want to continue and log in to your Telegram account? (y/Y to confirm): ").strip()
    if answer.lower() != "y":
        print("⏹️  Login cancelled. Run the program again when ready.")
        sys.exit(0)

    # Step 4: Login and create session
    await create_session()


if __name__ == "__main__":
    asyncio.run(run_setup())