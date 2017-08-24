import random

def binary_search(list, query):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == query:
            return mid
        elif query < guess:
            high = mid - 1
        else:
            low = mid + 1
    return -1
    

my_list = range(0, 2000);

for x in range(1, 100):
    query = random.randint(0, 2500)
    search_index = binary_search(my_list, query)
    print(f"*** {query} is at index: {search_index}" )
    
