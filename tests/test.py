import unittest
from src.main import *

client = create_client()


class Config(unittest.TestCase):

    def test_username_valid(self):
        info = harvest_by_username(client, 'ghazale_nrz')
        self.assertEqual(info['username'], 'ghazale_nrz')
        self.assertEqual(info['phone'], '989388488825')
        self.assertEqual(info['first_name'], "Ghazale")
        self.assertEqual(info['bio'], 'bio')

    def test_username_not_valid(self):
        # Channel
        self.assertEqual(harvest_by_username(client, 'zahra'),
                         'This username either belongs to a channel or a group')
        # Group
        self.assertEqual(harvest_by_username(client, 'hi_group'),
                         'This username either belongs to a channel or a group')
        # None-existent username
        self.assertEqual(harvest_by_username(client, 'sdlkjflasjf'),
                         'This username does not exist')
        # Phone number with no telegram account
        self.assertEqual(harvest_by_phone(client, '+989372639717'),
                         'There is no account connected to this phone number')
        # Nonsense
        self.assertEqual(harvest_by_phone(client, 'johowfoiej'),
                         'There is no account connected to this phone number')


if __name__ == '__main__':
    unittest.main(client)
