from telethon import TelegramClient, events, sync
from telethon.tl import functions
from telethon.errors import SessionPasswordNeededError
import Config


def harvest(username):
    api_id = Config.api_id
    api_hash = Config.api_hash
    phone = Config.phone
    user_id = Config.user_id
    client = TelegramClient(user_id, api_id, api_hash)
    client.start()

    entity = client.get_entity(username)
    print("id: ", entity.__getattribute__("id"))
    print("access_hash: ", entity.__getattribute__("access_hash"))
    print("first_name: ", entity.__getattribute__("first_name"))
    print("last_name: ", entity.__getattribute__("last_name"))
    print("phone: ", entity.__getattribute__("phone"))
    print("status: ", entity.__getattribute__("status").stringify())
    print("photo", entity.__getattribute__("photo"))


def sign_in():
    pass
    # client.send_message('1286407260', 'Hello! Talking to you from Telethon')
    # client.download_profile_photo('ijustwannatestthis')
    # messages = client.get_messages('username')
    # messages[0].download_media()
    #
    # @client.on(events.NewMessage(pattern='(?i)hi|hello'))
    # async def handler(event):
    #     await event.respond('Hey!')


def main():
    print("Please enter telegram username:")
    username = 'ijustwannatestthis'
    harvest(username)


if __name__ == '__main__':
    main()
