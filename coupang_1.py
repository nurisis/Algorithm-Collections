

my_map = {"spy" : 3, "s" : 4, "h" : 1}
my_map = sorted(my_map.items())
print(my_map)

my_map.sort(key = lambda item: item[1], reverse=True)
# my_map = sorted(my_map.items(), key = lambda item: item[1], reverse=True)
print(my_map)
# key = lambda item: len(item[0])
