# class Car:
#     def __init__(self, model, year, color, for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
    
#     #Instances dont need the param as they are already in class
#     def drive(self):
#         print(f"You drive {self.model}")

#     def stop(self):
#         print(f"You stopped {self.model}")
    
#     def describe(self):
#         print(f"{self.year} {self.color} {self.model}")
# class Truck(Car):#can use (Car) the param to pass the init and all the functions inside to call it for another 
#     def drive(self):
#         print(f"You Drive Big Truck!, {self.model}")
# class SuperCar(Car):#can use (Car) the param to pass the init and all the functions inside to call it for another

#     def drive(self):
#         print(f"You Drive One Exotic Car, {self.model}")
# class Start:
#     def start(self):
#         print(f"This Car is Starting")
# class Stop:
#     def stop(self):
#         print(f"This car is stopping")
# class Car2(Start, Stop):
#     pass
    
# car3 = Car2

# car1 = Car("M5", 2024, "red", False)

# car2 = Car("Corvette", 2025, "blue", True)

# truck = Truck("F-150", 2021, "Black", True)

# supercar = SuperCar("LaFerrari", 2019, "Rosa Red", False)

# print(truck)
# print(car1.model)
# print(car1.year)
# print(car1.color)
# print(car1.for_sale)
# print(car2.model)

# car9 = Car2()

# truck.drive()

# car2.drive()

# car1.stop()

# car1.describe()

# print(truck.model)

# truck.drive()

# print(supercar.for_sale)

# print(supercar.year)

# supercar.drive()

# car9.start()

# car9.stop()
# from typing import Dict, List


# def create_grid(rows: int, cols: int, value: int) -> List[List[int]]:
    
#     return [[value] * cols for _ in range(rows)]

    


# # do not modify below this line
# print(create_grid(2, 3, 0))
# print(create_grid(3, 2, 1))
# print(create_grid(4, 4, 4))
# print(create_grid(1, 1, 5))
# print(create_grid(1, 5, 5))

# grid = [[[0] * 5 for _ in range(10)]] 
# # This Creates a nested list of 10 list and each list has five 0's

# grid = [[0] * 3] * 2

# grid[0][0] = 1

# print(grid) # [[1, 0, 0], [1, 0, 0]]

# grid = [[0 for i in range(3)] for j in range(2)]

# grid[0][0] = 1

# print(grid) # [[1, 0, 0], [0, 0, 0]]
        
# print(grid)

# grid = [
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# rows = len(grid)    # 2
# cols = len(grid[0]) # 3 Gets the length of the first row to get the lnegth of cols
# print(rows)
# print(cols)

# def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
#     res = {}

#     for key, value in zip(keys, values):
#         res[key] = value
#     return res

# print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
# #{'Alice': 90, 'Bob': 80, 'Charlie': 70} Output

from collections import defaultdict
from typing import Dict, List


def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    res = []

    for key in keys:
        res.append(hash_map[key]) 
    return res
#Appends the value assocaited with  the key in the second list keys with thee value of hashmap to res
print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))

dict = {"Alice": 90, "Bob": 80, "Charlie": 70}
key = ["Alice", "Bob", "Charlie"]
print(dict)
print(key)
my_dict = {'a': 1, 'b': 2}
#Deleting 
my_dict.pop('c', 'default') # No error, returns 'default
del my_dict['b'] # {}

print(my_dict)

name = "Sean"

print(name[:1])
print(name[1:])
print(name[:-1])
print(name[::-1])
#Output
# S
# ean
# Sea
# naeS

r = 5

print(r // 3) 
nums = [1, 2, 3, 4]
d = defaultdict(list)
for i in range(1, len(nums)):
    d["bruh"].append(nums[i])
print( d)