import unittest
import fuzzer_json
import pickle
import os

class unit_tests(unittest.TestCase):
    def test_cycle_list(self):
        lst = fuzzer_json.cykled_lst(0)
        with open('data.pkl', 'wb') as file:
        # Serialize the object and write it to the file
            pickle.dump(lst, file)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data = pickle.load(file)
        self.assertTrue(fuzzer_json.check_equal_list(lst,loaded_data),"List")
        os.remove("data.pkl")

    def test_cycle_dict(self):
        lst = fuzzer_json.cykled_dict(0)
        with open('data.pkl', 'wb') as file:
        # Serialize the object and write it to the file
            pickle.dump(lst, file)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data = pickle.load(file)
        self.assertFalse(fuzzer_json.check_equal_dict(lst,loaded_data),"Dict")
        os.remove("data.pkl")

    def test_double_cycle_list(self):
        list1 = [0]
        list2 = [1]
        list3 = [list1,list2]
        list2.append(list3)
        list1.append(list2)

        with open('data.pkl', 'wb') as file:
        # Serialize the object and write it to the file
            pickle.dump(list1, file)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data = pickle.load(file)
        
        self.assertEqual(str(list1),str(loaded_data))
        os.remove("data.pkl")

    def sets(self):
        set = {}
        os.remove("data.pkl")

    def nested_class(self):
        os.remove("data.pkl")
        pass

    def list_test(self):
        os.remove("data.pkl")
        pass
    
    def dict_test(self):
        os.remove("data.pkl")
        pass
    
    def sets_test(self):
        os.remove("data.pkl")
        pass

    def class_unorganised(self):
        os.remove("data.pkl")
        pass

if __name__ == '__main__':
    unittest.main()

