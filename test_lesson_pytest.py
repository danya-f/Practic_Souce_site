import pytest
import requests
from faker import Faker
from pprint import pprint



BASE_URL = 'https://restful-booker.herokuapp.com/booking'
STATUS_OK = 200

@pytest.fixture()
def booking_id():
    add_book = {
        "firstname": "Klava",
        "lastname": "Bulk",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-10-10",
            "checkout": "2023-10-17"
        },
        "additionalneeds": "Breakfast"}
    response = requests.post(BASE_URL, json=add_book)
    booking_id = response.json()['bookingid']
    yield booking_id

def test_get_all_bookings(): #запрашиваем айди всех букингов
    zapros = requests.get(BASE_URL)
    print("вывод обычного запроса гет")
    print(zapros)
    assert zapros.status_code == STATUS_OK
    print('CODE VIVOD')
    pprint(zapros.status_code,)
    print('вывод запроса гет в виде джесон')
    pprint(zapros.json())
    assert 'Connection' in zapros.headers.keys()

def test_get_booking_with_id():
    expect_keys  = ['bookingdates' , 'depositpaid' ,  'firstname' , 'lastname' , 'totalprice']
    otvet = requests.get(f'{BASE_URL}/1')
    print(otvet)
    response_date = otvet.json()
    print(response_date)
    pprint(response_date)
    assert otvet.status_code == STATUS_OK
    for i in expect_keys:
        assert i in response_date.keys()
    assert response_date['depositpaid'] == True

def test_create_booking():
    add_book =  {
    "firstname" : "Patricia",
    "lastname" : "Bulk",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2023-10-10",
        "checkout" : "2023-10-17"
    },
    "additionalneeds" : "Breakfast"}
    response = requests.post(BASE_URL , json=add_book)
    pprint(response.json())
    assert  response.status_code == STATUS_OK
    id = response.json()['bookingid']
    get_response =  requests.get(f'{BASE_URL}/{id}').json()
    assert get_response['firstname'] == 'Patricia'

def test_get_booking_id_with_fixture(booking_id):
    response = requests.get(f'{BASE_URL}/{booking_id}')
    assert response.status_code == STATUS_OK
    assert response.json()['firstname'] == 'Klava'

fake = Faker()
a = fake.items()
print(a)