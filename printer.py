## programers.co.kr
## stack/queue - 프린터

def solution(priorities, location):
    answer = 0
    ind = 0
    queue_length = len(priorities)
    while(True):
        max_ind = ind
        max_value = priorities[ind]
        for i in range(queue_length):
            if max_value < priorities[(i+ind)%queue_length]:
                max_ind = (i+ind)%queue_length
                max_value = priorities[(i+ind)%queue_length]
                
        if max_ind == location:
            return answer+1
        elif max_ind < location:
            location -= 1
            
        del priorities[max_ind]
        queue_length -= 1
        ind = max_ind%queue_length
        answer += 1

