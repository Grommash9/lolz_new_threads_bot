import requests

from app import config


def send_data(message):
    for users in config.target_users:
        requests.get(
            f'https://api.telegram.org/bot{config.bot_token}/sendMessage?chat_id={users}&text={message}&parse_mode=html')
