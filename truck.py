## programers.co.kr
## stack/queue - 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    timer = [0] * len(truck_weights)
    bridge_current_weight = 0
    waiting = [0] * len(truck_weights)
    count = 0
    stopflag = 0
    answer = 0
    while(True):
        answer += 1
        if count > len(truck_weights)-1:
            count = len(truck_weights)-1
            stopflag = 1
        for i in range(len(waiting)):
            if waiting[i] == 1:
                timer[i] += 1 
            if timer[i] >= bridge_length and waiting[i] != 2:
                waiting[i] += 1
                bridge_current_weight -= truck_weights[i]
                
        if weight >= bridge_current_weight+truck_weights[count] and not stopflag:
            bridge_current_weight += (truck_weights[count])
            waiting[count] += 1
            count += 1
        
        if sum(waiting) >= 2*len(waiting):
            break
    return answer
