import pytest
from core.pi_connection import *

class TestIntegration:
    def test_update_endpoint(self):
        pass

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