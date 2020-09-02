from telethon import TelegramClient, events, sync
from telethon.tl import functions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.errors import SessionPasswordNeededError
import Config


def harvest(username):
    host_api_id = Config.api_id
    host_api_hash = Config.api_hash
    host_user_id = Config.user_id
    client = TelegramClient(host_user_id, host_api_id, host_api_hash)
    client.start()

    # entity = client.get_entity(username)
    entity = client(GetFullUserRequest(username))
    user = entity.__getattribute__("user")
    print(entity)
    print("id: ", user.__getattribute__("id"))
    print("access_hash: ", user.__getattribute__("access_hash"))
    print("first_name: ", user.__getattribute__("first_name"))
    print("last_name: ", user.__getattribute__("last_name"))
    print("phone: ", user.__getattribute__("phone"))
    print("status: ", user.__getattribute__("status"))

    photo = client.download_profile_photo(username)
    print("photo location: ", photo)

    print("bio: ", entity.__getattribute__("about"))


def main():
    username = input('Please enter telegram username:')
    harvest(username)


if __name__ == '__main__':
    main()
