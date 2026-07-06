numbers = [x for x in range(5)]
print(numbers)

def square(x):
    return x*x

squares = list(map(lambda x: x*x, range(5)))
print(squares)
print([square(x) for x in range(5)])

even_numbers = [x for x in range(5) if x%2==0]
odd_numbers = [x for x in range(6) if x%2!=0]
print(even_numbers)
print(odd_numbers)

even_list = [x if x%2==0 else -x for x in range(5)]
print(even_list)

# 딕셔너리
my_dict={}
my_dict["apple"]=1
my_dict["banana"]=2
my_dict["orange"]=3

key = "apple"
if key in my_dict:
    value = my_dict[key]
    print(f"{key} : {value}")
else:
    print("찾는 key없음")

my_dict["banana"]=4
print(my_dict)

del my_dict["orange"]
print(my_dict)

# 딕셔너리 생성
my_new_dict = {"apple":1, "banana":2, "cherry":3}

# key값은 키위
key="apple"
# key가 dict에 있는지 확인
if key in my_new_dict:
    print(f"값: {my_new_dict[key]}")
# 없으면 패쓰
else:
    print("찾는 key값 없음")

# 빈 셋 생성
empty_set = set()
print(empty_set) # set() 출력

#리스트 -> 튜플
list_to_set = set([1,2,3,4,5])
print(list_to_set)

#중괄호 이용한 셋
set_from_braces = {14,15,1,4}
print(set_from_braces)

# 문자열 set
string_to_set={"h","e","l","l","o"}
string_set=set("hello")
print(string_to_set," ",string_set)

#튜플을 셋으로 변환
tuple_to_set=set((1,2,4,4,6,3,5))
print(tuple_to_set)

comprehension_set={x for x in range(5) if x%2==0}
print(comprehension_set)

#셋에 원소 추가할 떄는 add나 update를 사용함
#add는 원소 하나, update는 여러개

my_set={1,2,3,4}
my_set.add(5)
print(my_set)

my_set.update([5,6,7,8])
print(my_set)

#셋에서 원소 제거부분 (remove -> 원소없음 오류발생, discard-> 원소없어도 오류발생안함)
my_set = {1,2,3,4}
print(my_set)

my_set.remove(2)
print(my_set)

# 2가 없는데 또 2를 remove하면 error
# my_set.remove(2)
# print(my_set)
my_set.discard(2) # 오류발생 X
print(my_set) 

#모든 원소 제거
my_set.clear()
print(my_set) #set() 출력

#합집합 구하기 (union 메서드, | 사용)
set1={1,2,3}
set2={4,5,6}

#union메서드 사용
print(set1.union(set2))
# | 연산자 사용
set1|=set2
print(set1)

# 교집합 -> intersection 사용
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}
set1 = set1.intersection(set2)
print(set1)

# &을 사용해도 됨
set1 &= set2
print(set1)

#차집합은 differenece 나 -
set1 = {1,2,3}
set2 = {3,4,5}
difference_set=set1.difference(set2)
print(difference_set)
print(set1-set2)