import sender_stand_requests
import data

def test_order():

    # создание заказа
    request_result = sender_stand_requests.post_create_order();

    # Проверяется, что код ответа равен 201 (заказ создан)
    assert request_result.status_code == 201

    # Сохраняем трек номер заказа из ответа
    track_number = request_result.json()["track"]
    
    # Получение заказа по его трек номеру
    request_result = sender_stand_requests.get_order_by_track(track_number)

    # Проверяется, что код ответа равен 200 (запрос успешно выполнен)
    assert request_result.status_code == 200

    # Проверяем, что в ответе есть поле order
    assert request_result.json()['order'] is not None

    # Проверяем, что есть сооьветсвующие поля в ответе
    order = request_result.json()['order']
    assert order['firstName'] == data.order_data['firstName']
    assert order['phone'] == data.order_data['phone']
