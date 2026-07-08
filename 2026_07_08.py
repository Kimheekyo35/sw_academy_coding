# list, tuple -> 처음부터 훑기 때문에 O(N)
# dict, set -> 해시로 한번에 찾아서 O(1)

# 우선 입력값은 [1,2,3,4,5]
def solution(answers):
    patterns = [
        [1,2,3,4,5], # -> pattern, 길이: len(pattern)
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    
    scores = [0 for _ in range(len(patterns))]
    # patterns의 길이는 정해져있기 때문에 O(N*M) 이라 시간복잡도는 N^2이 아니다.
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores[j] += 1
    
    max_score = max(scores)

    # result_list = [0 for _ in range(n)] 을 하게되면 [1,0,0] 이렇게 나올 수 있음
    result_list = []
    for i, sco in enumerate(scores):
        if sco == max_score:
            result_list.append(i+1)
    
    return sorted(result_list)

print(solution([1,3,2,4,2]))