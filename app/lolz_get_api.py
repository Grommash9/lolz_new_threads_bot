import json
import time
import requests
from app import config, tg, data_base


def get_updates():
    for forums in config.forums_list:
        url = f"https://api.lolz.guru/threads?forum_id={forums}"

        headers = {
            'Authorization': f'Bearer {config.access_token}'
        }

        response = requests.request("GET", url, headers=headers)
        json_response = response.json()

        for threads in json_response['threads']:
            if threads['first_post']['post_create_date'] > time.time() - 3600:
                if data_base.add_thread(threads['thread_id']):

                    tg.send_data(f"<b>Новая тема!</b> от {threads['creator_username']}\n"
                                 f"------------------------------\n"
                                 f"{threads['thread_title']}\n"
                                 f"------------------------------\n"
                                 f"{threads['first_post']['post_body_plain_text'][:3800]}\n\n"
                                 f"{threads['links']['permalink']}")
                    time.sleep(1)
        time.sleep(5)
