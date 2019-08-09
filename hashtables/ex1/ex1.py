#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        # hash_table_remove,
                        hash_table_retrieve,
                        # hash_table_resize
                        )
                        
# Pseudocode:
# 1. loop: insert each item in list into HT
# 2. loop: find difference -> difference = limit - value in weight list
# 3. if there are other items in HT (storage > 0), check if any keys equal the difference 
# 4. so pass difference as key in retrieve function
# 5. if retrieve functions returns a value (which is the index), save it
# 6. return it in tuple with the iterator i, which is the value we want to return - find max/min values
# 7. return None if result never found

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    
    result = None

    for i in range(length): # 1
        hash_table_insert(ht, weights[i], i ) # 1
        
    for i in range(length): # 2
        difference = limit - weights[i] # 2

        if len(ht.storage) > 0: # 3

            if hash_table_retrieve(ht, difference) != None: # 4
                other_value = hash_table_retrieve(ht, difference) # 5

                result = (max([i, other_value]), min([i, other_value])) # 6
               
                return result # 6

    return result # 7

    # O(2n) --> O(n)



def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")




# TESTING

# def returnTuple():
#     a = (2, 7)
#     return a

# print(returnTuple())

weights1 = [ 4, 6, 10, 15, 16 ]
answer_1 = get_indices_of_item_weights(weights1, len(weights1), 21)
print(answer_1) # (3, 1)


weights_2 = [4, 4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
print(answer_2) # (1, 0)