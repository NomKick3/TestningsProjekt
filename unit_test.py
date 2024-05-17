import unittest
import testing
import fuzzer_json
import pickle
import nested_class

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

    def test_double_cycle_list(self):
        pass

    def test_sets(self):
        pass

    def test_nested_class(self):
        outer = nested_class.OuterClass()
        inner = outer.InnerClass()
        inner.messege('test')

        with open('data.pkl', 'wb') as file1:
        # Serialize the object and write it to the file
            pickle.dump(inner, file1)
        with open('data.pkl', 'rb') as file1:
            # Deserialize the object from the file
            loaded_data1 = pickle.load(file1)
        
        self.assertEqual(inner, loaded_data1)

        with open('data.pkl', 'wb') as file2:
        # Serialize the object and write it to the file
            pickle.dump(outer, file2)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data2 = pickle.load(file2)

        self.assertEqual(outer, loaded_data2)


    def test_list(self):
        pass
    
    def test_dict(self):
        pass
    
    def test_sets(self):
        pass

    def test_class_unorganised(self):
        unorg1 = nested_class.Unorganised()
        unorg1.x = 3
        unorg1.y = 4

        unorg2 = nested_class.Unorganised()
        unorg2.y = 4
        unorg2.x = 3

        with open('data.pkl', 'wb') as file1:
        # Serialize the object and write it to the file
            pickle.dump(unorg1, file1)
        with open('data.pkl', 'wb') as file2:
        # Serialize the object and write it to the file
            pickle.dump(unorg2, file2)

        self.assertEqual(file1, file2)

        with open('data.pkl', 'rb') as file1:
            # Deserialize the object from the file
            loaded_data1 = pickle.load(file1)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data2 = pickle.load(file2)
        
        self.assertEqual(unorg1, loaded_data1)
        self.assertEqual(unorg2, loaded_data2)

        
    


