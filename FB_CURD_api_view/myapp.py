import requests
import json

URL = "http://127.0.0.1:8000/stuapi/"

#this function is use to RETRIVE data in console
def get_data(id = None):
    data = {}
    if id is not None:
        data ={'id':id}
    headers ={'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.get(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)

#get_data()

#this function is use to POST data
def post_data():
    data = {
        'name':'jesh',
        'roll':'105',
        'city':'indore'
    }

    '''for the api_view we have to use headers'''
    headers={'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers=headers, data=json_data)
    data = r.json()
    print(data)
#post_data()



#this function is use to UPDATE data
def update_data():
    data = {
        'id':4,
        'name':'ali',
        'city':'dewas'
    }
    '''for the api_view we have to use headers'''
    headers={'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers=headers,data=json_data)
    data = r.json()
    print(data)
#update_data()



#this function is use to DELETE data
def delete_data():
    data = {'id': 4}
    headers={'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers=headers,data=json_data)
    data = r.json()
    print(data)
#delete_data()
