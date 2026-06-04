import re

from main import client, events

# -------- Handle incoming messages --------
@client.on(events.NewMessage(chats="@YoutubeFiler_bot"))
async def handler(event):
    try:
        text = event.raw_text

        if event.buttons:
            await event.click(2)  # Click the second button (Download)

        elif event.video and event is not None:
            print("Received media message type video .")

            filename = re.sub(r'[\\/*?:"<>|]', "_", text)
            print(f" video title serialized with regex (text) : {filename}")
            print("start downloading video...")

            try:
                await event.download_media(file=f"./static/{filename}.mp4")
                print("Downloaded successfully")

            except Exception as e:
                print(f"Download failed: {e}")

        elif text:
            print("Received:", text)

    except Exception as e:
        print(f"ERROR: {e}")

