from rubpy import Client
import asyncio

# GUID اکانت روبیکا (اینجا جایگذاری کن)
GUID = "weoylmmtfiugvirugovlrumyxikzfytd"  # <--- GUID خودت رو اینجا بذار

client = Client(name='MikeyBot')

@client.on_message_updates()
async def handle_start(update):
    message = update.message
    text = message.text or ""

    # فقط به /start جواب بده (در پی‌وی و گروه)
    if text.strip() == '/start':
        await message.reply('سلام من مایکی هستم 😻')

async def main():
    print("ربات مایکی در حال راه‌اندازیه...")
    await client.connect()
    await client.login(guid=GUID)
    print("ربات مایکی با موفقیت شروع شد! (در گروه و پی‌وی کار می‌کنه)")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())
