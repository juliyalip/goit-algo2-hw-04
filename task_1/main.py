from network_data import (SINK, SOURCE, build_logistics_network)
from report import (calculate_store_totals, 
                    calculate_terminal_store, 
                    calculate_terminal_totals,
                    print_algorithm_steps, print_totals, verify_results,
                    print_logistic_edges, print_terminal_store_table
                      )

def main():
    network = build_logistics_network()

    max_flow, flow, steps = network.edmonds_karp(
        SOURCE,
        SINK
    )

    print(f"Maximum flow: {max_flow}")
    print_algorithm_steps(steps)

    terminal_store_flow = calculate_terminal_store(steps)

    print_terminal_store_table(terminal_store_flow)

    terminal_totals = calculate_terminal_totals(terminal_store_flow)

    store_totals = calculate_store_totals(terminal_store_flow)
    print_totals(terminal_totals, store_totals)

    verify_results(max_flow, terminal_totals)


if __name__=="__main__":
    main()