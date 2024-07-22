from collections import defaultdict

def hashmap(str): #the output of this function is list
    map = defaultdict(list)
    result=[] #this should be returned

    for i in str:
        sorted_S = tuple(sorted(i))
        map[sorted_S].append(i)
    for val in map.values():
        result.append(val)
    return result


print(hashmap(['eat','ate','bil','lib','axe']))
