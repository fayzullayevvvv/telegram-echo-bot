import time

import requests

from config import TOKEN



class Bot:
    
    def __init__(self, token: str):
        self.BASE_URL = f'https://api.telegram.org/bot{token}'
        self.offset = None

    def get_updates(self):
        get_updates_url = f'{self.BASE_URL}/getUpdates'

        params = {
            'offset': self.offset,
            'limit': 20
        }
        response = requests.get(get_updates_url, params=params)

        if response.status_code == 200:
            return response.json()['result']
        else:
            raise Exception('Telegram server xatolik qaytardi!')
        
    def send_message(self, chat_id: str, text: str):
        send_message_url = f'{self.BASE_URL}/sendMessage'

        params = {
            'chat_id': chat_id,
            'text': text
        }

        requests.post(send_message_url, data=params)
        
    def send_photo(self, chat_id: str, file_id: str):
        send_message_url = f'{self.BASE_URL}/sendPhoto'

        params = {
            'chat_id': chat_id,
            'photo': file_id
        }

        requests.post(send_message_url, data=params)

    def run(self):
        while True:
            updates = self.get_updates()
            for update in updates:
                self.offset = update['update_id'] + 1
                message = update.get('message')
                if not message:
                    continue

                chat_id = message['chat']['id']

                if 'text' in message:
                    self.send_message(chat_id, message['text'])

                elif 'photo' in message:
                    self.send_photo(chat_id, message['photo'][-1]['file_id'])

            time.sleep(1)
bot = Bot(TOKEN)
bot.run()