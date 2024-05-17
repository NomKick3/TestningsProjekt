import unittest
import fuzzer_json
import pickle
import os
import nested_class
import random
import sys

sys.setrecursionlimit(10000)
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
        empty_list = []
        random_list = [random.randint(0, 100) for i in range(10)]
        same_value_list = [5] * 10
        sorted_list = sorted([3, 1, 4, 1, 5, 9, 2, 6]) 
        mixed_list = [1, 'apple', 3.14, True, None]
        nested_list = [[1, 2, 3], ['a', 'b', 'c'], [True, False]]
        large_list = list(range(10000))
        negative_list = [-1, -5, -10, -15, -20]

         # Compare pickled lists
        self.assertTrue(self.compare_pickled(empty_list), "Empty list pickling failed")
        self.assertTrue(self.compare_pickled(random_list), "Random list pickling failed")
        self.assertTrue(self.compare_pickled(same_value_list), "Same value list pickling failed")
        self.assertTrue(self.compare_pickled(sorted_list), "Sorted list pickling failed")
        self.assertTrue(self.compare_pickled(mixed_list), "Mixed list pickling failed")
        self.assertTrue(self.compare_pickled(nested_list), "Nested list pickling failed")
        self.assertTrue(self.compare_pickled(large_list), "Large list pickling failed")
        self.assertTrue(self.compare_pickled(negative_list), "Negative list pickling failed")
        os.remove("data.pkl")     

    def compare_pickled(self,original):
        pickled = pickle.dumps(original)
        loaded = pickle.loads(pickled)
        if(loaded == original):
            return True
        os.remove("data.pkl")
        return False
    
    def test_pick_pickle(self):
        lst = [1, 'apple', 3.14, True, None]
        pickled = pickle.dumps(lst)
        second_pickled = pickle.dumps(pickled)
        loaded = pickle.loads(second_pickled)
        second_loaded = pickle.loads(loaded)
        self.assertEqual(lst, second_loaded)
    
    def test_dict(self):
        dict1 = {}
        dict2 = {'string': 'test', 1:0, 'int': 1, 'float': 1.5, 'bool': True, 'Nan': None}
        dict3 = {'list': []}
        dict4 = {'dict':{}}

        with open('data.pkl', 'wb') as file1:
        # Serialize the object and write it to the file
            pickle.dump(dict1, file1)
        with open('data.pkl', 'rb') as file1:
            # Deserialize the object from the file
            loaded_data1 = pickle.load(file1)
        
        self.assertEqual(dict1, loaded_data1)

        with open('data.pkl', 'wb') as file2:
        # Serialize the object and write it to the file
            pickle.dump(dict2, file2)
        with open('data.pkl', 'rb') as file2:
            # Deserialize the object from the file
            loaded_data2 = pickle.load(file2)

        self.assertEqual(dict2, loaded_data2)

        with open('data.pkl', 'wb') as file3:
        # Serialize the object and write it to the file
            pickle.dump(dict3, file3)
        with open('data.pkl', 'rb') as file3:
            # Deserialize the object from the file
            loaded_data3 = pickle.load(file3)
        
        self.assertEqual(dict3, loaded_data3)

        with open('data.pkl', 'wb') as file4:
        # Serialize the object and write it to the file
            pickle.dump(dict4, file4)
        with open('data.pkl', 'rb') as file4:
            # Deserialize the object from the file
            loaded_data4 = pickle.load(file4)

        self.assertEqual(dict4, loaded_data4)
        os.remove("data.pkl")

    def test_tuples(self):
        tuple1 = ()
        tuple2 = tuple(x for x in range(random.randint(0,1000)))
        tuple3 = tuple('Unittesting')
        tuple4 = (0, (1, (2, (3, (4, (5, (0)))))))
        tuple5 = (1, 1.2, 'test', True, None)
        tuple6 = ({}, [])

        with open('data.pkl', 'wb') as file1:
        # Serialize the object and write it to the file
            pickle.dump(tuple1, file1)
        with open('data.pkl', 'rb') as file1:
            # Deserialize the object from the file
            loaded_data1 = pickle.load(file1)
        
        self.assertEqual(tuple1, loaded_data1)

        with open('data.pkl', 'wb') as file2:
        # Serialize the object and write it to the file
            pickle.dump(tuple2, file2)
        with open('data.pkl', 'rb') as file2:
            # Deserialize the object from the file
            loaded_data2 = pickle.load(file2)

        self.assertEqual(tuple2, loaded_data2)

        with open('data.pkl', 'wb') as file3:
        # Serialize the object and write it to the file
            pickle.dump(tuple3, file3)
        with open('data.pkl', 'rb') as file3:
            # Deserialize the object from the file
            loaded_data3 = pickle.load(file3)
        
        self.assertEqual(tuple3, loaded_data3)

        with open('data.pkl', 'wb') as file4:
        # Serialize the object and write it to the file
            pickle.dump(tuple4, file4)
        with open('data.pkl', 'rb') as file4:
            # Deserialize the object from the file
            loaded_data4 = pickle.load(file4)

        self.assertEqual(tuple4, loaded_data4)

        with open('data.pkl', 'wb') as file5:
        # Serialize the object and write it to the file
            pickle.dump(tuple5, file5)
        with open('data.pkl', 'rb') as file5:
            # Deserialize the object from the file
            loaded_data5 = pickle.load(file5)
        
        self.assertEqual(tuple5, loaded_data5)

        with open('data.pkl', 'wb') as file6:
        # Serialize the object and write it to the file
            pickle.dump(tuple6, file6)
        with open('data.pkl', 'rb') as file6:
            # Deserialize the object from the file
            loaded_data6 = pickle.load(file6)

        self.assertEqual(tuple6, loaded_data6)
        os.remove("data.pkl")
            
    
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
        os.remove("data.pkl")

    def test_types(self):
        none = None # None
        tf = True # Bool
        notcircle = Ellipsis # ??? Ellipsis
        func = NotImplemented # ??? NotImplemented
        number = 137848345 # Integers
        decimal_number = 132123.123123123 # Float point numbers
        cnumber = 5 + 4j # ??? Complex Numbers
        sanntext = "Amanda är dryg som fan" # Strings
        brb = bytes('bytestesting', 'utf-8') # Bytes
        brb_array = bytearray([1, 2 ,3, 4])# Byte Arrays
        types = [none,tf,notcircle,func,number,decimal_number,cnumber,sanntext,brb,brb_array]
        names = ["None","Bool","Ellipsis","NotImplemented","Int","Float","Complex","String","Bytes","Byte Array"]
        with open("data.pkl","w") as file:
            for type,name in zip(types,names):
                pickle.dump(type,file)
                loaded_data = pickle.load(file)
                self.assertEqual(type, loaded_data, name)


        os.remove("data.pkl")

if __name__ == '__main__':
    unittest.main()
