import os

import network


def _show_menu(message):
    if message:
        print(message)

    print('1. Ping')
    print('2. List pings')
    print('3. Exit')
    print()


def _is_valid(cmd):
    return cmd in ['1', '2', '3']


def _run(cmd):
    if cmd == '1':
        return network.ping()

    if cmd == '2':
        network.list_pings()

    if cmd == '3':
        exit()


def init():
    message = ''
    while True:
        _show_menu(message)

        cmd = input('Enter a number').strip()
        if _is_valid(cmd):
            message = _run(cmd)

