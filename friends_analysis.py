import urllib.request
import urllib.parse
import urllib.error
import twurl
import json
import ssl

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py


def get_json_file(username, amount):
    """
    This function returns information about twitter account under the given username

    :param username: str
    :param amount: str
    :return: dict
    """

    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    if len(username) < 1 or int(amount) < 1:
        return None
    url = twurl.augment(TWITTER_URL,{'screen_name': username, 'count': amount})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data, encoding='utf-8')
    return js


def friends_info(js, key):
    """
    This function returns specific(key) information about user's friends

    :param js: dict
    :param key: str
    :return: list
    """
    info = []

    for user in js['users']:
        if key not in user:
            return None
        if key != 'name':
            info.append((user['name'], user[key]))
        elif key == 'name':
            info.append(user[key])
    return info


if __name__ == '__main__':
    username = input("Please enter username: ")
    amount = input("Please enter amount: ")
    key = input("Please enter key: ")
    js = get_json_file(username, amount)
    info = friends_info(js, key)
    if js == None or info == None:
        print('One of your inputs was wrong. Please restart the program.')
        exit()
    for el in info:
        if key != 'name':
            print('name: '+str(el[0])+'; '+key+': '+str(el[1]))
        elif key == 'name':
            print('name: '+str(el))
