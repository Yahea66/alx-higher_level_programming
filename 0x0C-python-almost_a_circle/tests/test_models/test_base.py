import unittest
import os
import json
from unittest.mock import patch
from models.base import Base
from models.square import Square

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        base1 = Base()
        base2 = Base(12)
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 12)
        self.assertEqual(base3.id, 2)

    def test_json_string_conversion(self):
        dict_list = [{'id': 10}, {'id': 20}]
        json_string = Base.to_json_string(dict_list)
        self.assertEqual(json_string, json.dumps(dict_list))
        self.assertEqual(Base.to_json_string([]), '[]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_to_file_none_empty(self):
        Base.save_to_file(None)
        self.assertTrue(os.path.exists('Base.json'))
        with open('Base.json', 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_from_json_string(self):
        json_string = '[{"id": 10}, {"id": 20}]'
        objects = Base.from_json_string(json_string)
        self.assertEqual(objects, [{'id': 10}, {'id': 20}])
        self.assertEqual(Base.from_json_string(''), [])
        self.assertEqual(Base.from_json_string(None), [])
        

    def test_load_from_file_non_existent(self):
        if os.path.exists('Base.json'):
            os.remove('Base.json')
        self.assertEqual(Base.load_from_file(), [])

    def test_load_from_file_existent(self):
        with open('Base.json', 'w') as f:
            f.write('[{"id": 1, "size": 10, "x": 2, "y": 3}]')
        with patch('models.base.Base.create') as mocked_create:
            Base.load_from_file()
            mocked_create.assert_called_with(id=1, size=10, x=2, y=3)

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove('Base.json')
        except OSError:
            pass
