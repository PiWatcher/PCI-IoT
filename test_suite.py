import pytest
from core.load_model import *
from platform import python_version
import os
from core.pi_connection import *
import datetime

HOME_PATH = os.getenv("HOME")

class TestUnit:
    def test_loaded_model(self):
        loaded_model = load_model()
        assert loaded_model != -9999

    def test_setup(self):
        assert python_version() == '3.7.9'
        assert os.path.isdir(f'{HOME_PATH}/env')
    
    def test_set_env(self):
        assert_list = []
        assert_list.append('BLDGNAME' in os.environ)
        assert_list.append('BLDGNUM' in os.environ)
        assert_list.append('ROOMNUM' in os.environ)
        assert_list.append('ENDPOINTID' in os.environ)
        assert_list.append('ROOMCAP' in os.environ)
        assert_list.append('IPADDRESS' in os.environ)

        assert all([item==True for item in assert_list])

class TestIntegration:
    def test_update_endpoint(self):
        responce = {"status": 200,
                    "timestamp": datetime.datetime.now(),
                    "message": f"[Egr (90)] (EPID_1) successfully added it's entry"}

        assert responce['status'] == 200

    def test_json_for_endpoint(self):
        test_count = 20
        bool_list = []
        json_str = generate_json(test_count)
        for key, value in json_str.items():
            if key == 'count':
                bool_list.append(type(value) is int)
            else:
                bool_list.append(type(value) is str)

        assert all([item==True for item in bool_list])