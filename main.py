import asyncio
import os
import random
import re
import sys

from dotenv import load_dotenv
from telethon import TelegramClient, events

ENV_FILE = ".env"
SESSION_FILE = "my_session.session"
output_path = './static'

# -------- Auto-setup if .env or session is missing --------
async def ensure_setup():
    if not os.path.exists(ENV_FILE) or not os.path.exists(SESSION_FILE):
        print("⚙️  First-time setup required...")
        from setup import run_setup
        await run_setup()
        print("\n✅ Setup complete! Starting the main program...\n")


# -------- Load env --------
load_dotenv()
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient("my_session", api_id, api_hash) if (api_id and api_hash) else None
download_done = asyncio.Event()


# -------- Function to send messages --------
async def send_message(username: str | int, message: str, client: TelegramClient):
    await client.send_message(username, message)

    delay = random.uniform(4, 8)
    print(f"Waiting {delay:.1f}s before next action...")
    await asyncio.sleep(delay)


# -------- Handle incoming messages --------
def register_handlers(client: TelegramClient):
    @client.on(events.NewMessage(chats="@YoutubeFiler_bot"))
    async def handler(event):
        global output_path
        try:
            text = event.raw_text

            if event.buttons:

                stored_first_button=False
                for row_index, row in enumerate(event.buttons):
                    for col_index, button in enumerate(row):
                        print(f"[{row_index}][{col_index}] → '{button.text}'")
                        if not stored_first_button :
                            first_btn=str(button.text)
                            stored_first_button=True

                target_text = "720p"
                clicked = False

                for row in event.buttons:
                    for button in row:
                        if target_text.lower() in button.text.lower():
                            await asyncio.sleep(random.uniform(2, 5))
                            await button.click()
                            clicked = True
                            break
                    if clicked:
                        break

                if not clicked: # not found the 720p mp4 quuality. so click on first button
                    print(f"⚠️ Button with text '{target_text}' not found!")
                    print('click on first button')
                    for row in event.buttons:
                        for button in row:
                            if first_btn.lower() in button.text.lower():
                                await asyncio.sleep(random.uniform(2, 5))
                                await button.click()
                                clicked = True
                                break

                            if clicked:
                                break

                if not clicked:
                    print("not button i think is there.")


            elif event.video and event.file:
                print("Received media message type video.")

                filename = re.sub(r'[\\/*?:"<>|]', "_", text)
                print(f"Video title serialized with regex (text): {filename}")
                print(f"Start downloading video:\n\t {filename}.mp4")

                try:
                    os.makedirs( output_path , exist_ok=True)
                    opath = os.path.join(output_path, filename)
                    await event.download_media(file=f"{opath}.mp4")
                    print("Downloaded successfully")

                except Exception as e:
                    print(f"Download failed: {e}")
                    sys.exit(1)

                finally:
                    download_done.set()

            elif text:
                print("Received:", text)

        except Exception as e:
            print(f"ERROR: {e}")


# -------- Read file --------
def read_links_from_file(file_path: str) -> list:
    try:
        with open(file_path) as f:
            return f.read().splitlines()

    except Exception as e:
        print(f"Error reading file: {e}")
        return []


# -------- Run the client --------
async def main():
    global output_path
    # Auto-setup check before anything else
    await ensure_setup()

    # Re-load env in case setup just created it
    load_dotenv(override=True)
    api_id = os.getenv("API_ID")
    api_hash = os.getenv("API_HASH")

    if not api_id or not api_hash:
        print("❌ API credentials not found. Run setup again.")
        sys.exit(1)

    # Parse CLI arguments
    if len(sys.argv) > 1 and sys.argv[1] != "-l":

        urls = read_links_from_file(file_path=sys.argv[-1])

        if '-o' in sys.argv:
            output_dir_index = sys.argv.index('-o') + 1
            output_path = sys.argv[output_dir_index]
            print(f"Output directory set to: {output_path}")
            os.makedirs(output_path, exist_ok=True)


    elif "-l" in sys.argv:
        n = sys.argv.index("-l")
        urls = [sys.argv[n + 1]]

        if '-o' in sys.argv:
            output_dir_index = sys.argv.index('-o') + 1
            output_path = sys.argv[output_dir_index]
            print(f"Output directory set to: {output_path}")
            os.makedirs(output_path, exist_ok=True)

    else:
        raise RuntimeError("""No file path provided.
Please provide the path to the file containing YouTube links as a command-line argument.
Example usage:
    python3 main.py /path/to/your/links.txt
OR if you have only one link:
    python3 main.py -l <URL>
""")

    # Build client and register handlers
    tg_client = TelegramClient("my_session", int(api_id), api_hash)
    register_handlers(tg_client)

    await tg_client.start()

    for downloaded_video_count, url in enumerate(urls, start=1):
        download_done.clear()
        await send_message("@YoutubeFiler_bot", str(url), tg_client)
        await download_done.wait()

        # if url is the last url in urls , do not wait for 20 or 50 seconds
        if downloaded_video_count < len(urls) - 1:
            await asyncio.sleep(random.uniform(20, 50))

    print("\n\nAll Downloads Done")
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
