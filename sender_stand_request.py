import requests
import configuration

#Создание нового заказа
def create_order(body):
     return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                          json=body)

#Получение заказа по его номеру
def get_order_by_its_track(track_number):
     return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_ITS_TRACK,
                         params={"t": track_number})

