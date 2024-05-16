import random
import pickle
import json
import orjson
import msgspec
from tqdm import tqdm
from graph import Graph
import sys
import fuzzer_json


def random_data_generator():
    # while True:
      #  g = Graph()
       # g.generate_nodes(1000)
        #g.generate_graph(100000)
        #Syield g
     return fuzzer_json.random_data_generator()

def main():
    sys.setrecursionlimit(1000000)
    random.seed(9001)
    data_generator = random_data_generator()
    exeptions = []
    mismatches = []
    for _ in tqdm(range(1000)):
        data = next(data_generator)
        try:
            with open('data.pkl', 'wb') as file:
            # Serialize the object and write it to the file
                pickle.dump(data, file)
            with open('data.pkl', 'rb') as file:
            # Deserialize the object from the file
                loaded_data = pickle.load(file)
            
        except Exception as exception:
            exeptions += [(exception, data)]
        else:
            pass
            if not loaded_data == data:
                print(loaded_data,data)
                mismatches += [data]
    print(f'{len(exeptions)} exceptions and {len(mismatches)} mismatches found')
    print(exeptions)

if __name__ == '__main__':
    main()
