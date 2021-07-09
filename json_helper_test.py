import json
from unittest import TestCase

import json_helper, pickle




# python3 -m unittest json_helper_test
class Test_Json_Helper(TestCase):

    def test_read_json(self):
        result = json_helper.read_json('/Users/sean/labs/PyPart9/data/super_smash_bros/mario.json')
        valueDict = {
        "name": "Mario",
        "neutral_special": "Fireball",
        "side_special": "Cape",
        "up_special": "Super Jump Punch",
        "down_special": "F.L.U.D.D.",
        "final_smash": "Mario Finale"

    
        }
        self.assertEqual(result, valueDict)
    
    def test_read_all_json_files(self):
        result = json_helper.read_all_json_files('/Users/sean/labs/PyPart9/data/super_smash_bros copy')
        valueList = [{
        "name": "Mario",
        "neutral_special": "Fireball",
        "side_special": "Cape",
        "up_special": "Super Jump Punch",
        "down_special": "F.L.U.D.D.",
        "final_smash": "Mario Finale"
        }]

        self.assertEqual(result, valueList)

    
    def test_write_pickle(self):
        expected = [{
        "name": "Mario",
        "neutral_special": "Fireball",
        "side_special": "Cape",
        "up_special": "Super Jump Punch",
        "down_special": "F.L.U.D.D.",
        "final_smash": "Mario Finale"
}]

        #
        json_helper.write_pickle('/Users/sean/labs/PyPart9/data/super_smash_bros copy')
        with open('/Users/sean/labs/PyPart9/**super_smash_characters.pickle**', 'rb') as f:
           a = pickle.load(f)
        #print(a)
        self.assertEqual(expected, a)


    def test_load_pickle(self):
        actual = json_helper.load_pickle('/Users/sean/labs/PyPart9/**super_smash_characters.pickle**')
        expected = str({'name': 'Mario', 'final_smash': 'Mario Finale', 'down_special': 'F.L.U.D.D.', 'side_special': 'Cape', 'up_special': 'Super Jump Punch', 'neutral_special': 'Fireball'})
        self.assertEqual(actual, expected)
        

