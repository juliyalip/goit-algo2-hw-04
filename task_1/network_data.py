from flow_network import FlowNetwork

SOURCE = "Source"
SINK = "Sink"

TERMINALS = [
    "Terminal 1",
    "Terminal 2"
]

STORES = [
    f"Store {number}" for number in range (1,15)
]

STORE_CAPACITIES ={
    "Store 1": 15,
    "Store 2": 10,
    "Store 3": 20, 
    "Store 4": 15,
    "Store 5": 10,
    "Store 6": 25,
    "Store 7": 20,
    "Store 8": 15,
    "Store 9": 10,
    "Store 10": 20,
    "Store 11": 10,
    "Store 12": 15,
    "Store 13": 5,
    "Store 14": 10,
}

LOGISTIC_EDGES =[
  ("Terminal 1", "Warehouse 1", 25),
  ("Terminal 1", "Warehouse 2", 20),
  ("Terminal 1", "Warehouse 3", 15),
  ("Terminal 2", "Warehouse 3", 15),
  ("Terminal 2", "Warehouse 4", 30),
  ("Terminal 2", "Warehouse 2", 10),

   ("Warehouse 1", "Store 1", 15),
   ("Warehouse 1", "Store 2", 10),
   ("Warehouse 1", "Store 3", 20),

   ("Warehouse 2", "Store 4", 15),
   ("Warehouse 2", "Store 5", 10),
   ("Warehouse 2", "Store 6", 25),

   ("Warehouse 3", "Store 7", 20),
   ("Warehouse 3", "Store 8", 15),
   ("Warehouse 3", "Store 9", 10),

   ("Warehouse 4", "Store 10", 20),
   ("Warehouse 4", "Store 11", 10),
   ("Warehouse 4", "Store 12",15),
   ("Warehouse 4", "Store 13", 5),
   ("Warehouse 4", "Store 14", 10),

]

def build_logistics_network():
    network = FlowNetwork()

    network.add_edge(SOURCE, "Terminal 1", 60 )
    network.add_edge(SOURCE, "Terminal 2", 55 )

    for start, end, capacity in LOGISTIC_EDGES:
        network.add_edge(start, end, capacity)

    for store, capacity in STORE_CAPACITIES.items():
        network.add_edge(store, SINK, capacity)
    
    return network
