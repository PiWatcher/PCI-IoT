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
#my_json_string = json.dumps({'key1': val1, 'key2': val2})
def main():
    print(len(sys.argv))
    if len(sys.argv) != 6:
        print("No bueno muchacho")
        return
    #print(sys.argv[4])
    date_time = str(datetime.datetime.now())
    print(type(date_time))
    json_str = {
        "timestamp": date_time,
        "building_id": sys.argv[1],
        "building": sys.argv[2],
        "endpoint_id": sys.argv[3],
        "endpoint": sys.argv[4],
        "count": sys.argv[5]
    }
    json_obj = json.dumps(json_str)
    print(type(json_str))
    
    url = 'http://127.0.0.1:5000/api/update'
    print(url);
    x = requests.post(url, json = json_str)
    print(json_obj);
    print(x.text)
    
    
if __name__ == "__main__":
    main()