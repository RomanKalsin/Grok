def ind_lowest_cost_node(costs): # Узел с наименьшей стоимостью
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
graph = {"start": {"A": 6, "B": 2},
         "A": {"finish": 1},
         "B": {"A": 3, "finish": 5},
         "finish": {}}
coast = {"A": 6, "B": 2, "finish": float("inf")}
parents = {"A": "start", "B": "start", "finish": None}
processed = []
node = ind_lowest_cost_node(coast)
while node is not None:
    cost = coast[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_coast = cost + neighbors[n]
        if coast[n] > new_coast:
           coast[n] = new_coast
           parents[n] = node
    processed.append(node)
    node = ind_lowest_cost_node(coast)
print(coast)
print(parents)