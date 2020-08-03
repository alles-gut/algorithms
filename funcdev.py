## programers.co.kr
## stack/queue - 기능개발

import math
def solution(progresses, speeds):
    answer = []
    done = [0] * (len(progresses)+1)
    for i in range(len(progresses)):
        done[i] = 101 - math.ceil((100-progresses[i])/speeds[i])
    
    count = 0
    for i in range(len(done)-1):
        if done[i-count] <= done[i+1]:
            count += 1
            continue
        else:
            answer.append(count+1)
            count = 0
    
    return answer
