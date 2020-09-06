##########
# Array
##########
from bisect import bisect_left, bisect_right

n = 10
empty_list = [2] * n
print(empty_list)

array = [1, 2, 3, 4, 5]
print(f"-1 : {array[-2]}")

array[-1] = 6
print(f"change :{array}")
print(f"list[1:4] : {array[1:4]}")

array = [i * i for i in range(1, 10)]
print(f"array : {array}")

# append. O(1)
array.append(100)
print(f"after append : {array}")

# insert at specific index. O(N)
array.insert(1, 1)
# remove. O(N) => When you want to use remove(), do like below
removed_after = [i for i in array if i != 100]
print(f"removed_after : {removed_after}")

# count specific data. O(N)
num_of_1 = array.count(1)
print(f"num_of_1 : {num_of_1}")

# sort O(N)
array.sort(reverse=False)
print(f"after sort : {array}")

# N x M dimension array
n = 5
m = 2
array = [[0] * m for _ in range(n)]
print(f"N x M : {array}")

##########
# String
##########
# concat strings
a = "HI"
b = "THERE"
merged = a + " " + b
print(f"merged:{merged}")
print(f"triple : {a * 3}")

# string slicing
print(f"merged[1:2] : {merged[1:2]}")

##########
# Tuple
##########
# Can't change a data in tuple.
tuple = (1, 2, 3, 4)

##########
# Dictionary
# Inside, it consists of HashTable => O(1) for searching or editing
##########
data = dict()
data['key1'] = 'value1'
data['key2'] = 'value2'
data['key3'] = 'value3'
print(f"data : {data}")

# get all keys
keys = data.keys()
print(f"keys : {keys}")
# get all values
values = data.values()
print(f"values :{values}")

##########
# Set
# No duplicate / No order
# add, remove O(1)
##########
set_a = set({1, 2, 3, 4, 5})
set_b = {1, 3, 5, 7, 9, 11}
# add
set_a.add(6)
# add multiple
set_a.update({7, 8, 9})
# remove
set_a.remove(9)

# sum
print(f"sum : {set_a | set_b}")
# intersection
print(f"intersection : {set_a & set_b}")
# difference
print(f"difference : {set_b - set_a}")

##########
# Python standard library
##########

sum([1, 2, 3])
min(1, 2, 3, 4)
max(1, 2, 3, 4)
cal_result = eval("(3+5)*7")  # 56
print(f"cal_result : {cal_result}")

# sort by specific standard
result = sorted([('A', 35), ('B', 22), ('C', 45)], key=lambda x: x[1])
print(f"sorted : {result}")

# 'iertools' -> permutations(순열), combinations(조합)
data = ['A', 'B', 'C']

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement

# every case of 'len(data)'P'r'
permutation_result = list(permutations(data, r=3))
print(f"permutation_result : {permutation_result}")
# every case of 'len(data)'C'r'
combination_result = list(combinations(data, r=2))
print(f"combination_result : {combination_result}")
# every case of 'len(data)'P'repeat' & allow duplicate
product_result = list(product(data, repeat=2))
print(f"product_result : {product_result}")
# every case of 'len(data)'C'r' & allow duplicate
replacement_result = list(combinations_with_replacement(data, r=2))
print(f"replacement_result : {replacement_result}")

import heapq


# heap =>  priority queue.
# ascending sort with min heap
def min_heap_sort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))

    return result


# descending sort with max heap
def max_heap_sort(iterable):
    h = []
    result = []

    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))

    return result


heap_result = max_heap_sort([1,3,5,7,6,4,2])
print(f"heap_result: {heap_result}")


# bisect - binary search
a = [1, 2, 4, 4, 8]
x = 4
# Find the leftmost index in list a to insert data x into, maintaining sorted order
print(bisect_left(a, 4))
# Find the rightmost index in list a to insert data x into, maintaining sorted order
print(bisect_right(a, 4))

