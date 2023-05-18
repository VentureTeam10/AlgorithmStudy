#다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    total_weight = 0
    
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        total_weight -= bridge.popleft()
        
        if total_weight + truck_weights[0] <= weight:
            truck = truck_weights.popleft()
            bridge.append(truck)
            total_weight += truck
        else:
            bridge.append(0)
        
        answer += 1
    
    answer += bridge_length  
    return answer
