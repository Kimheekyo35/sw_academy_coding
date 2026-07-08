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


arr1=[[1,4],[3,2],[4,1]] # 3행 2열
arr2=[[3,5],[3,5]] # 2행 2열


# 어차피 크기가 같을테니
r1, c1 = len(arr1), len(arr1[0])
r2, c2 = len(arr2), len(arr2[0])

# 두 행렬의 곱은 arr1의 행과 arr2의 열
# 담을 것
new_list= [[0]*c2 for _ in range(len(arr1))]

# r1 = 3, c1 = 2, r2 = 2, c2 = 2
# c1, r2 는 결국 같을 값
for i in range(r1): # 3
    for j in range(c2): #2
        for k in range(c1): # =r2
            new_list[i][j] += arr1[i][k] * arr2[k][j]
print(new_list)


# 행렬 곱 함수
def solution(arr_1, arr_2):
    r1, c1 = len(arr_1), len(arr_1[0])
    r2, c2 = len(arr_2), len(arr_2[0])

    result_list = [[0]* c2 for _ in range(r1)]

    for i in range(r1):#arr_1 행
        for j in range(c2): # arr_2열
            for k in range(r2): #arr_1열 = arr_2 행
                result_list[i][j] += arr_1[i][k] * arr_2[k][j]

    return result_list


print(solution([[2,3,2],[4,2,4],[3,1,4]],[[5,4,3],[2,4,1],[3,1,1]]))


stages = [2,1,2,6,2,4,3,3]
N = 5
result_list = []

total = len(stages) #8
for i in range(1,N+1):
    count = stages.count(i)
    total -= count
    quarter = count / total
    print(count,total,"  ",quarter)
    result_list.append(quarter)
    