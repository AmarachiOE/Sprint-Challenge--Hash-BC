#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        # hash_table_remove,
                        hash_table_retrieve,
                        # hash_table_resize)


# Pseudocode:
# 1. loop: tickets and insert each ticket in HT
# 2. retrieve value in HT where key == None, meaning the first ticket of trip
# 3. make that first item in route array
# 4. loop: starting at second slot in route array range(1, length):
# 5. pass the item before as the key in ht retrieval to get next item
# 6. save value, and set as the current (ith) item in route array
# 7. return route

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(length): # 1
        hash_table_insert(ht, tickets[i].source, tickets[i].destination )

    first_item = hash_table_retrieve(ht, "NONE") # 2
    route[0] = first_item # 3

    for i in range(1, length): # 4
        next_item = hash_table_retrieve(ht, route[i-1]) # 5
        # if next_item != 'NONE':
        route[i] = next_item # 6
        print("Updated Route: ", route)

    return route # 7

# O(2n) -> O(n)

# TESTING

tickets1 = [
  Ticket("PIT", "ORD"),
  Ticket("XNA", "CID"),
  Ticket("SFO", "BHM"),
  Ticket("FLG", "XNA"),
  Ticket("NONE", "LAX"),
  Ticket("LAX", "SFO"),
  Ticket("CID", "SLC"),
  Ticket("ORD", "NONE"),
  Ticket("SLC", "PIT"),
  Ticket("BHM", "FLG")
]

reconstruct_trip(tickets1, len(tickets1))

# ["LAX", "SFO", "BHM", "FLG", "XNA", "CID", "SLC", "PIT", "ORD", "NONE"]