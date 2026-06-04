from telethon import TelegramClient, events
import asyncio
from dotenv import load_dotenv
import os
import re

# -------- Load variables from .env file --------
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("my_session", api_id, api_hash)


# -------- Function to send messages --------
async def send_message(username: str | int , message: str):
    await client.send_message(username, message)

# -------- Handle incoming messages --------
@client.on(events.NewMessage(chats='@YoutubeFiler_bot'))
async def handler(event):
    try:
        text = event.raw_text

        if event.buttons:
            await event.click(2) # Click the second button (Download)

        elif event.video and event.file:
            print("Received media message type video .")
            
            filename = re.sub(r'[\\/*?:"<>|]', "_", text)
            print(f" video title serialized with regex (text) : {filename}")
            print('start downloading video...')

            try:
                await event.download_media(
                    file=f"./static/{filename}.mp4"
                )
                print("Downloaded successfully")

            except Exception as e:
                print(f"Download failed: {e}")
        
        elif text:
            print("Received:", text)

        
    except Exception as e:
        print(f"ERROR: {e}")
# -------- Run the client --------
async def main():
    await client.start()

    await send_message("@YoutubeFiler_bot", 
                       "https://www.youtube.com/watch?v=AiqSS4XFkSI")


    # await send_message("@YoutubeFiler_bot",
    #  "https://www.youtube.com/watch?v=kbq_4t7De_Y")

    # await send_message("@YoutubeFiler_bot",
    #   "https://www.youtube.com/watch?v=6D8MdVTyqd4")

    await client.run_until_disconnected()


if __name__ == "__main__":
    asyncio.run(main())