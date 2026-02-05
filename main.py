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
    
    def send_voice(self, chat_id: str, file_id: str):
        send_voice = f'{self.BASE_URL}/sendVoice'

        params = {
            'chat_id': chat_id,
            'voice': file_id
        }

        requests.post(send_voice, data=params)
    
    def send_video_note(self, chat_id: str, file_id: str):
        send_video_note_url = f'{self.BASE_URL}/sendVideoNote'

        params = {
            'chat_id': chat_id,
            'video_note': file_id
        }

        requests.post(send_video_note_url, data=params)

        
    def send_photo(self, chat_id: str, file_id: str):
        send_photo_url = f'{self.BASE_URL}/sendPhoto'

        params = {
            'chat_id': chat_id,
            'photo': file_id
        }

        requests.post(send_photo_url, data=params)

    def send_video(self, chat_id: str, file_id: str):
        send_video_url = f'{self.BASE_URL}/sendVideo'

        params = {
            'chat_id': chat_id,
            'video': file_id
        }

        requests.post(send_video_url, data=params)

    def send_animation(self, chat_id: str, file_id: str):
        send_animation_url = f'{self.BASE_URL}/sendAnimation'

        params = {
            'chat_id': chat_id,
            'animation': file_id
        }

        requests.post(send_animation_url, data=params)

    def send_audio(self, chat_id: str, file_id: str):
        send_audio_url = f'{self.BASE_URL}/sendAudio'

        params = {
            'chat_id': chat_id,
            'audio': file_id
        }

        requests.post(send_audio_url, data=params)

    def send_document(self, chat_id: str, file_id: str):
        send_document_url = f'{self.BASE_URL}/sendDocument'

        params = {
            'chat_id': chat_id,
            'document': file_id
        }

        requests.post(send_document_url, data=params)

    def send_sticker(self, chat_id: str, file_id: str):
        send_sticker_url = f'{self.BASE_URL}/sendSticker'

        params = {
            'chat_id': chat_id,
            'sticker': file_id
        }

        requests.post(send_sticker_url, data=params)

    def send_location(self, chat_id: str, latitude: float, longitude: float):
        send_location_url = f'{self.BASE_URL}/sendLocation'

        params = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude
        }

        requests.post(send_location_url, data=params)

    def send_poll(self, chat_id: str, question: str, options: list):
        send_poll_url = f'{self.BASE_URL}/sendPoll'

        params = {
            'chat_id': chat_id,
            'question': question,
            'options': options,
            'is_anonymous': False
        }

        requests.post(send_poll_url, json=params)

    def send_poll(self, chat_id: str, question: str, options: list):
        send_poll_url = f'{self.BASE_URL}/sendPoll'

        params = {
            'chat_id': chat_id,
            'question': question,
            'options': options,
            'is_anonymous': False
        }

        requests.post(send_poll_url, json=params)



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
                
                elif 'voice' in message:
                    self.send_voice(chat_id, message['voice']['file_id'])

                elif 'video_note' in message:
                    self.send_video_note(chat_id, message['video_note']['file_id'])

                elif 'photo' in message:
                    self.send_photo(chat_id, message['photo'][-1]['file_id'])

                elif 'video' in message:
                    self.send_video(chat_id, message['video']['file_id'])

                elif 'animation' in message:
                    self.send_animation(chat_id, message['animation']['file_id'])

                elif 'audio' in message:
                    self.send_animation(chat_id, message['audio']['file_id'])

                elif 'document' in message:
                    self.send_document(chat_id, message['document']['file_id'])

                elif 'sticker' in message:
                    self.send_sticker(chat_id, message['sticker']['file_id'])

                elif 'location' in message:
                    location = message['location']
                    self.send_location(chat_id, location['latitude'], location['longitude'])

                elif 'poll' in message:
                    self.send_poll(chat_id, message['poll']['question'], [i['text'] for i in message['poll']['options']])

            time.sleep(1)


bot = Bot(TOKEN)
bot.run()