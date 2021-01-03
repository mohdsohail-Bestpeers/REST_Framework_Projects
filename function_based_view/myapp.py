import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"

#this function is use to RETRIVE data in console
def get_data(id = None):
    data = {}
    if id is not None:
        data ={'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data=json_data)
    data = r.json()
    print(data)

#get_data()

#this function is use to POST data
def post_data():
    data = {
        'name':'alfiza',
        'roll':'104',
        'city':'jawra'
    }
    headers ={'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers ,data=json_data)
    data = r.json()
    print(data)
#ost_data()



#this function is use to UPDATE data
def update_data():
    data = {
        'id':5,
        'name':'alfaiz',
        'city':'laduna'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL,data=json_data)
    data = r.json()
    print(data)
#update_data()



#this function is use to DELETE data
def delete_data():
    data = {'id': 5}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,data=json_data)
    data = r.json()
    print(data)
#delete_data()
