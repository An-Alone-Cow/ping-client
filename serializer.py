import os

def _is_valid(content):
    for char in content:
        if char not in '0123456789:.- |':
            return False
    return True


def serialize(content):
    if _is_valid(content):
        return content.split('|')

    return ['Error, Invalid data recieved from server.']

