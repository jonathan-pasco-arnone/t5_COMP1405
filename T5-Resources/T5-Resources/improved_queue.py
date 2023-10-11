
def addend(list, dict, value):
    list.append(value)
    dict[value] = len(list) - 1 # The key is the value
    
def removestart(list,dict):
    if len(list) == 0:
        return None

    # Changes the keys in the dictionary to match the new order
    # overwriting the first person in queue effectively deleting them
    # Aka every key - 1
    print("\n\n\nstart")
    print(dict)
    print(list)
    quantity_keys = len(dict.keys()) - 1
    if quantity_keys == 0:
        del dict[0]
    else:
        for key in range(quantity_keys):
            dict[key] = dict[key + 1]
        print(dict)
        print(quantity_keys)
        del dict[quantity_keys]

    return list.pop(0)
    
def containslinear(list, value):
    return value in list
    
def containshash(dict, value):
    if dict.get(value) is None:
        return False
    return True






import random
import time
list = []
hash = {}
addprob = 100
removeprob = 90
repeat = 50000
maxval = 500
searchlist = []
#randomly build the data by probabilistically adding/removing items to the list
#also generate a list of items to search for later
#also make sure that the dictionary search is returning the same result as the list search
for i in range(repeat):
    if random.randint(0,100) < addprob:
        addend(list, hash, random.randint(0,maxval))
    if random.randint(0,100) < removeprob:
        removestart(list, hash)
        
    searchlist.append(random.randint(0,maxval))
    
    searchnum = random.randint(0,maxval)
    
    if containslinear(list, searchnum) != containshash(hash, searchnum):
        print("Error: dictionary and list search returned different results")
        exit()

start = time.time()
for i in searchlist:
    containslinear(list, i)
end = time.time()
print("Linear time: ", (end-start))

start = time.time()
for i in searchlist:
    containshash(hash, i)
end = time.time()
print("Hash time: ", (end-start))
