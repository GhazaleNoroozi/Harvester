from telethon.sync import TelegramClient
from telethon.tl.functions import users
from telethon.tl.types import User, Channel
from src import Config
import json


def x_str(s):
    if s is None:
        return 'UNAVAILABLE'
    return str(s)


def harvest_user(client, entity):
    """
    Retrieve and print information
    :param client: Telegram client
    :param entity: The target entity
    :return: None
    """
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

    info = '{"username": "' + x_str(username)\
           + '", "phone": "' + x_str(phone)\
           + '", "first_name": "' + x_str(first_name)\
           + '", "last_name": "' + x_str(last_name)\
           + '", "bio": "' + x_str(about)\
           + '", "last seen": "' + x_str(status)\
           + '", "photo": "' + x_str(photo_location) + '"}'

    json_info = json.loads(info)
    print(type(json_info))
    return json_info


def harvest_by_phone(client, phone):
    """
    Harvest user's information by phone number of there is an account connected to the phone number
    :param client: Telegram client
    :param phone: Target user phone number
    :return: None
    """
    try:
        entity = client(users.GetFullUserRequest(id=phone))
    except ValueError:
        return 'There is no account connected to this phone number'

    return harvest_user(client, entity)


def harvest_by_username(client, username):
    """
    Print information about the target user by creating a client
    :param client: The host client
    :param username: Target username
    :return None
    """
    try:
        entity = client.get_entity(username)
    except ValueError:
        return 'This username does not exist'

    if type(entity) == User:
        entity = client(users.GetFullUserRequest(id=username))
        return harvest_user(client, entity)
    elif type(entity) == Channel:
        return 'This username either belongs to a channel or a group'
    else:
        return 'This username does not belong to  a user, bot, channel or a group'


def create_client():
    """
    Create and connect a telegram client using information in Config.py file
    :return: Created client
    """
    host_api_id = Config.api_id
    host_api_hash = Config.api_hash
    host_user_id = Config.user_id
    host_phone = Config.phone

    client = TelegramClient(host_user_id, host_api_id, host_api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(host_phone)
        client.sign_in(host_phone, input('Enter code sent to your telegram: '))
    return client


def main():
    """
    Main method
    :return: None
    """

    client = create_client()
    code = input('Do you want to find the user based on username or phone number? [u/p] ')
    if code == 'u':
        res = harvest_by_username(client, input('Enter username: '))
        print(res)
    else:
        res = harvest_by_phone(client, input('Enter phone number (don\'t forget the country code): '))
        print(res)


if __name__ == '__main__':
    main()
