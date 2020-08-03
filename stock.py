## programers.co.kr
## stack/queue - 주식가격

def solution(prices):
    answer = [0] * len(prices)
    for i, p in enumerate(prices):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if p > prices[j]:
                break
    return answer
