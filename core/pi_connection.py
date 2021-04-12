import sys
import datetime
import json
import requests
from bson import json_util
import os

'''
"timestamp": "2020-11-18 13:47:39.716041",
    "building_id": "90",
    "building_name": "SICCS",
    "endpoint_id": "100",
    "endpoint_name": "Main Lobby",
    "count": 9
'''
def update_db(count):
    BldgName = os.getenv("BLDGNAME")
    BldgNum = os.getenv("BLDGNUM")
    RoomNum = os.getenv("ROOMNUM")
    EndPtId = os.getenv("ENDPTID")
    RoomCap = os.getenv("ROOMCAP")
    ip_addr = os.getenv("IPADDRESS")

    date_time = str(datetime.datetime.now())
    
    json_str = {
        "timestamp": date_time,
        "building_id": BldgNum,
        "building_name": BldgName,
        "endpoint_id": EndPtId,
        "room_name": RoomNum,
        "count": count,
        "room_capacity": RoomCap
    }

    #json_obj = json.dumps(json_str)

    json_obj = json.dumps(json_str, default=json_util.default)
    url = f'http://{str(ip_addr)}:5000/api/data/iot/update'
    print(json_obj)
    x = requests.post(url, json = json_str)
