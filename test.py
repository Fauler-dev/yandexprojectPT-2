# Заврикиди Глеб, 18 когорта — Дипломный проект. Инженер по тестированию +

import data
import request

def test_get_order_info_by_track():
    track = request.create_order(data.order_body).json()['track']
    response = request.get_order_info_by_track(track)
    assert response.status_code == 200