# Заврикиди Глеб, 18 когорта — Дипломный проект. Инженер по тестированию +

import requests
import config

def create_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER, json=body)

def get_order_info_by_track(track_number):
    get_order_url = f"{config.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response