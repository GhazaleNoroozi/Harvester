from telethon.sync import TelegramClient
from telethon.tl.functions import users
from telethon.tl.types import User, Channel
import Config


def harvest_user(client, entity):
    user = entity.__getattribute__("user")
    username = user.__getattribute__("username")
    photo_location = client.download_profile_photo(username)
    is_bot = user.__getattribute__('bot')
    about = entity.__getattribute__("about")
    tid = user.__getattribute__("id")
    access_hash = user.__getattribute__("access_hash")
    first_name = user.__getattribute__("first_name")
    last_name = user.__getattribute__("last_name")
    phone = user.__getattribute__("phone")
    status = user.__getattribute__("status")

    print('username: ', username,
          '\nid: ', tid,
          '\naccess_hash: ', access_hash,
          '\nis_bot: ', is_bot,
          '\nfirst_name: ', first_name,
          '\nlast_name: ', last_name,
          '\nphone number: ', phone,
          '\nbio: ', about,
          '\nstatus: ', status,
          '\nphoto file location: ', photo_location
          )


def harvest_by_phone(client, phone):
    try:
        entity = client(users.GetFullUserRequest(id=phone))
    except ValueError:
        print("There is no account connected to this phone number.")
        return

    harvest_user(client, entity)


def harvest_by_username(client, username):
    """
    Print information about the target user by creating a client
    :param client: The host client
    :param username: Target username
    """
    try:
        entity = client.get_entity(username)
    except ValueError:
        print("This username does not exist")
        return

    if type(entity) == User:
        entity = client(users.GetFullUserRequest(id=username))
        harvest_user(client, entity)
    elif type(entity) == Channel:
        print("This username either belongs to a channel or a group")
    else:
        print("This username does not belong to  a user, bot, channel or a group")


def main():
    host_api_id = Config.api_id
    host_api_hash = Config.api_hash
    host_user_id = Config.user_id
    host_phone = Config.phone

    client = TelegramClient(host_user_id, host_api_id, host_api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(host_phone)
        client.sign_in(host_phone, input('Enter code sent to your telegram: '))

    code = input('Do you want to find the user based on username or phone number? [u/p] ')
    if code == 'u':
        harvest_by_username(client, input('Enter username: '))
    else:
        harvest_by_phone(client, input('Enter phone number (don\'t forget the country code): '))


if __name__ == '__main__':
    main()
