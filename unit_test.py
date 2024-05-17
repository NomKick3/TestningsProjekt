import unittest
import fuzzer_json
import pickle
import os
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

    def test_nested_class(self):
        outer = nested_class.OuterClass()
        inner = outer.InnerClass()
        inner.write_messege('test')

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
        os.remove("data.pkl")

    def test_list(self):
        pass
    
    def test_dict(self):
        pass
    
    def test_sets(self):
        s1 = {"Random","Rando","Randy"}
        with open('data.pkl', 'wb') as file:
        # Serialize the object and write it to the file
            pickle.dump(s1, file)
        with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
            loaded_data = pickle.load(file)
        os.remove("data.pkl")

        self.assertEqual(s1,loaded_data)

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

if __name__ == '__main__':
    unittest.main()
