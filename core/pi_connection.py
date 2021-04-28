import sys
import datetime
import json
import requests
from bson import json_util
import os

'''
EXAMPLE JSON
"timestamp": "2020-11-18 13:47:39.716041",
    "building_id": "90",
    "building_name": "SICCS",
    "endpoint_id": "100",
    "room_name": "Main Lobby",
    "count": 9,
    "room_capacity": 50
'''

# Function: update_db
# INPUT ARGS:
# count - number of people
# Return: status code of api that was hit
def update_db(count):
    ip_addr = os.getenv("IPADDRESS")

    json_str = generate_json(count)

    json_obj = json.dumps(json_str, default = json_util.default)
    try:
        url = f'http://{str(ip_addr)}:5000/api/data/iot/update'
        print(json_str)
        x = requests.post(url, json = json_str)
    except:
        raise "Unable to hit backend API"

    print(x.json())
    return x.status_code

# Function: genertate_json
# INPUT ARGS:
# count - number of people
# Return: json string correctly formatted for endpoint 
def generate_json(count):
    BldgName = os.getenv("BLDGNAME")
    BldgNum = os.getenv("BLDGNUM")
    RoomNum = os.getenv("ROOMNUM")
    EndPtId = os.getenv("ENDPTID")
    RoomCap = os.getenv("ROOMCAP")

    date_time = datetime.datetime.now().isoformat()
    
    json_str = {
        "timestamp": date_time,
        "building_id": BldgNum,
        "building": BldgName,
        "endpoint_id": EndPtId,
        "endpoint": RoomNum,
        "count": int(count),
        "room_capacity": int(RoomCap)
    }

    return json_str

