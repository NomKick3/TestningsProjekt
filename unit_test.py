import unittest
import testing
import fuzzer_json
import pickle

class unit_tests(unittest.TestCase):
    def test_cycle_list(self):
        lst = fuzzer_json.cykled_lst(0)
        with open('data.pkl', 'wb') as file:
        # Serialize the object and write it to the file
            pickle.dump(lst, file)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data = pickle.load(file)
        self.assetFalse(fuzzer_json.check_equal(lst,loaded_data))

    def test_cycle_dict(self):
        lst = fuzzer_json.cykled_dict(0)
        with open('data.pkl', 'wb') as file:
        # Serialize the object and write it to the file
            pickle.dump(lst, file)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data = pickle.load(file)
        self.assetFalse(fuzzer_json.check_equal_list(lst,loaded_data))

    def double_cycle_list(self):
        pass

    def sets(self):
        pass

    def nested_class(self):
        pass

    def list_test(self):
        pass
    
    def dict_test(self):
        pass
    
    def sets_test(self):
        pass

    def class_unorganised(self):
        pass

    


