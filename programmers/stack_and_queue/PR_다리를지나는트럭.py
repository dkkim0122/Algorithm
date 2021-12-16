def solution(bridge_length, weight, truck_weights):
    trucks = [[truck, 0] for truck in truck_weights]
    bridge_on_truck = []
    finished_truck = []

    time = 0
    total_weight = 0
    while len(finished_truck) <= len(truck_weights):
        time += 1

        total_weight = sum(map(lambda x:x[0], bridge_on_truck))
        if trucks and trucks[0][0] + total_weight <= weight:
            bridge_on_truck.append(trucks.pop(0))
        
        for i in range(len(bridge_on_truck)):
            bridge_on_truck[i][1] += 1

        if bridge_on_truck[0][1] == bridge_length:
            finished_truck.append(bridge_on_truck.pop(0))

    time += 1

    return time
