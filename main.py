import asyncio
import os
import random
import re
import subprocess as subp
import sys

from dotenv import load_dotenv
from telethon import TelegramClient, events

# -------- Load variables from .env file --------
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("my_session", api_id, api_hash)
download_done = asyncio.Event()

# -------- Function to send messages --------
async def send_message(username: str | int, message: str, client: TelegramClient):
    await client.send_message(username, message)

    # -- delay --
    delay = random.uniform(4, 8)
    print(f"Waiting {delay:.1f}s before next action...")
    await asyncio.sleep(delay)


# -------- Handle incoming messages --------
@client.on(events.NewMessage(chats="@YoutubeFiler_bot"))
async def handler(event):
    try:
        text = event.raw_text

        if event.buttons:
            await asyncio.sleep(random.uniform(2, 5))
            await event.click(2)  # Click the second button (Download)

        elif event.video and event.file:
            print("Received media message type video .")

            filename = re.sub(r'[\\/*?:"<>|]', "_", text)
            print(f" video title serialized with regex (text) : {filename}")
            print(f"start downloading video:\n\t {filename}.mp4")

            try:
                await event.download_media(file=f"./static/{filename}.mp4")
                print("Downloaded successfully")

            except Exception as e:
                print(f"Download failed: {e}")
                exit()

            finally:
                download_done.set()

        elif text:
            print("Received:", text)

    except Exception as e:
        print(f"ERROR: {e}")


# --------  read file --------
def read_links_from_file(file_path: str) -> list:
    try:
        with open(file_path) as f:
            return f.read().splitlines()

    except Exception as e:
        print(f"Error reading file: {e}")
        return []


# -------- Run the client --------
async def main():
    if len(sys.argv) > 1 and sys.argv[1] != "-l":
        urls = read_links_from_file(file_path=sys.argv[1])

    elif "-l" in sys.argv:
        n = sys.argv.index("-l")
        urls = [sys.argv[n + 1]]

    else:
        raise RuntimeError("""No file path provided.
Please provide the path to the file containing YouTube links as a command-line argument.
Example usage:
    python3.xx main.py /path/to/your/links.txt
OR if you have only one link you can use:
    python3.xx main.py -l <URL>
""")
        exit(1)

    await client.start()

    downloaded_video_count = 0
    for url in urls:
        download_done.clear()  
        await send_message("@YoutubeFiler_bot", str(url), client)
        downloaded_video_count = 1 + downloaded_video_count
        await download_done.wait() 

        if downloaded_video_count == 10:
            print(f"the count of download of today reached {downloaded_video_count}.")
            print("end of program.")
            exit(0)

        await asyncio.sleep(random.uniform(40, 90))

    # await client.run_until_disconnected() 

    print("\n\nAll Downloads Done")
    exit(0)


if __name__ == "__main__":
    asyncio.run(main())
