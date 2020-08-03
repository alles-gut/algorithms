##programers.co.kr
##Hash - 완주하지 못한 선수

def solution(participant, completion):
    hash_table = {}
    count = 0
    for name in participant:
        count += hash(name)
        hash_table[hash(name)] = name
    for name in completion:
        count -= hash(name)
    return hash_table[count]
