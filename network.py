import os
from requests import get

import settings
import serializer


def ping():
    response = get(settings.url['ping'])

    if response.status_code == 200:
        return 'Ping Successful'
    else:
        return 'Ping Failed'


def _show_content(content):
    os.system('clear')
    for line in content:
        print(line)

    input('Press any key to go back to the menu...')


def list_pings():
    response = get(settings.url['list_pings'])

    content = serializer.serialize(response.content)
    _show_content(content)

