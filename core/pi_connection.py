import sys
import datetime
import json
import requests
'''
"timestamp": "2020-11-18 13:47:39.716041",
    "building_id": "90",
    "building_name": "SICCS",
    "endpoint_id": "100",
    "endpoint_name": "Main Lobby",
    "count": 9
'''
def update_db(ip_addr, endpoint_info):
    date_time = str(datetime.datetime.now())
    
    json_str = {
        "timestamp": date_time,
        "building_id": endpoint_info[0],
        "building_name": endpoint_info[1],
        "endpoint_id": endpoint_info[2],
        "endpoint_name": endpoint_info[3],
        "count": endpoint_info[4]
    }

    json_obj = json.dumps(json_str)
    print("Sending Data")
    url = f'http://{str(ip_addr)}:5000/api/data/update'
    print(json_obj)
    x = requests.post(url, json = json_obj)
    print("Data successfully sent")