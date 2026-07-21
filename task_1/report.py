from network_data import (LOGISTIC_EDGES, STORES, TERMINALS)

def print_algorithm_steps(steps):
    print("\nAlgorithm steps:")

    for number, path, added_flow, total_flow in steps:
        vertices = [path[0][0]]
       
        for start, end in path:
            vertices.append(end)

        path_text = " -> ".join(vertices)

        print(
            f"{number}. {path_text}; "
            f"Added flow: {added_flow}; "
            f"Total flow: {total_flow}"
        )

def print_logistic_edges(network, flow):
    print("\nFlow on logistic edges:")

    for start, end, _ in LOGISTIC_EDGES:
        current_flow = flow[(start, end)]
        capacity = network.capacity[(start, end)]

        print(
            f"{start} -> {end}"
            f"{current_flow}/{capacity}"
        )

def calculate_terminal_store(steps):
    terminal_store_flow ={}

    for terminal in TERMINALS:
        for store in STORES:
            terminal_store_flow[(terminal, store)] = 0
            
    for number, path, added_flow, total_flow in steps:
        vertices = [path[0][0]]

        for start, end in path:
            vertices.append(end)
        
        terminal = None
        store = None

        for vertex in vertices:
            if vertex in TERMINALS:
                terminal = vertex

            if vertex in STORES:
                store = vertex
        if terminal is not None and store is not None:
            terminal_store_flow[(terminal, store)] += added_flow
    return terminal_store_flow

def print_terminal_store_table(terminal_store_flow):
    print("\nFlow between terminals and stores:")

    print(
        f"{'Terminal':<15}"
        f"{'Store':<15}"
        f"{'Actual flow':>15}"
    )

    print("-" * 45)
    for terminal in TERMINALS:
        for store in STORES:
            actual_flow = terminal_store_flow[(terminal, store)]
    print(
        f"{terminal:<15}"
        f"{store:<15}"
        f"{actual_flow:>15}"
    )

def calculate_terminal_totals(terminal_store_flow):
    return {
        terminal: sum(
            terminal_store_flow[(terminal, store)] for store in STORES
        )
        for terminal in TERMINALS
    }

def calculate_store_totals(terminal_store_flow):
    return{
        store: sum(
            terminal_store_flow[(terminal, store)] for terminal in TERMINALS
        ) for store in STORES
    }

def print_totals(terminal_totals, store_totals):
    print("\nTotal flow from each terminal:")

    for terminal, total in terminal_totals.items():
        print(f"{terminal}: {total}")

    print("\nTotal flow received by each store:")
    for store, total in store_totals.items():
        print(f"{store}: {total}")

def verify_results(max_flow, terminal_totals):
    flow_from_table = sum(terminal_totals.values())

    print(f"Maximum flow: {max_flow}")
    print(f"Flow calculated from the table: {flow_from_table}")

    if flow_from_table == max_flow:
        print("The terminal-store flow table is correct")
        return True
    print("Error: the table does not match the maximum flow.")
    return False