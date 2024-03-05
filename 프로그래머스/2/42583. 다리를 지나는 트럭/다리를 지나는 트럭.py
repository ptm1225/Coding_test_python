def solution(bridge_length, weight, truck_weights):
    bridge = []
    time = []
    count = 0
    while bridge or truck_weights:
        time = [i-1 for i in time]
        count += 1
        
        if time and time[0] == 0:
            bridge.pop(0)
            time.pop(0)
        
        if truck_weights and sum(bridge) + truck_weights[0] <= weight:
            bridge.append(truck_weights.pop(0))
            time.append(bridge_length)
        
    return count