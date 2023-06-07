import requests
from pprint import pprint
import json

def get_data():
    """
    Get ten user data from randomuser API

    Returns:
        list: list of user data
    """
    users = []

    for i in range(10):
        url = "https://randomuser.me/api/"
        response = requests.get(url)
        results = response.json()['results'][0]
        name = results['name']
        first_name = name['first']
        last_name = name['last']
        phone = results['phone']
        city = results['location']['city']
        email = results['email']

        data = {
            "first_name": first_name,
            "last_name": last_name,
            "phone": phone,
            "city": city,
            "email": email
        }
        users.append(data)

        print(i)

    return users

def saveData(data, file_path):
    """
    Save data to a file

    Args:
        data (list): list of user data
        file_path (str): path to file
    """
    f = open(file_path, mode='w')
    data = json.dump(data, f, indent=4)
    f.close()

data = get_data()
saveData(data, 'data.json')