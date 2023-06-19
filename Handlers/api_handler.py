import requests
from Handlers.base_handler import BaseHandler


class ApiHandler(BaseHandler):
    def __init__(self, api_url):
        self.api_url = api_url
    def get_data(self):
        return requests.get(self.api_url)

    def set_data(self, data):
        url_orig = self.api_url
        for element in data:
            msg_id = int(element['msg_id'])
            msg_desc = element['msg_desc']
            msg_moderate_status = element['msg_moderate_status']
            msg_processed = element['msg_processed']
            data = {
                'msg_moderate_status': msg_moderate_status,
                'msg_processed': msg_processed
            }
            url = url_orig + f'{msg_id}/'
            print(url)
            response = requests.put(url, data=data)
            print(response.status_code)