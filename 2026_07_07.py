# tuple은 리스트, 딕셔너리와 달리 한 번 생성하면 삽입하거나 삭제 불가능
# 코딩테스트에서 '값이 바뀌지 않아야 한다'라는 조건이 있을 때 tuple 사용하면 정확

my_tuple=(1,2,3)
print(my_tuple[0])
print(my_tuple[1])
print(my_tuple[2])

print(my_tuple[:1])
print(my_tuple[:2])
print(my_tuple[1:2])

# 문자열은 큰따옴표, 작은 따옴표로 사용 가능
string1="Hello, World!"
string2='Hello, World!'

make_string = "Hello"
make_string += ", World!"
print(make_string)

string_list=["He","llo"]
print("".join(string_list))

num_list=[1,2,3]
print(" ".join(map(str,num_list)))

# 문자열을 수정하고 싶을 땐 replace() 메서드 사용
new_string="Hello"
new_string=new_string.replace("l","")
print(new_string)

#함수 정의
def add(num1,num2):
    return num1+num2

print(add(3,5))

# lambda 식: "익명 함수" 라고도 함. 이름이 없는 함수를 말하며 코드에서 딱 한 번 실행할 목적으로 사용.
add = lambda x,y:x+y
print(add(5,4))

ext = lambda x,y:x-y
print(ext(6,3))

num_list = [1,2,3,4,5]
squares = list(map(lambda x:x**2, num_list))
print(squares)


# 조기 반환 (early return)
def total_price(quantity, price):
    total = quantity*price
    if total > 100:
        return total * 0.9
    return total

print(total_price(4,50))

# 보호 반환 (numbers가 빈 값이거나 리스트가 아님 반환하라는)
def calculate_average(numbers):
    if numbers is None:
        return None
    
    if not isinstance(numbers,list):
        return None
    
    if len(numbers)==0:
        return None
    
    total = sum(numbers)
    average = total/len(numbers)
    return average

# def 함수를 사용해서 lambda 함수 만들기
def add_three(x):
    return x+3

def square(x):
    return x*x

composed_func = lambda x: square(add_three(x))
# 이렇게 하면 composed_func 한번만 호출한 걸로 볼 수 있음 (유지보수 쉬움)
print(composed_func(5))

arr = [0,0,0,0,0,0]
arr = [0]*6
print(arr)

arr = list(range(5))
print(arr)

arr_0 = [0 for _ in range(5)]
print(arr_0)

# 2차원 배열
arr_2 = [[1,2,3,4,5],[6,7,8,9,10]]
print(arr_2[1][3]) #9
arr_2[1][3]=15
print(arr_2)

arr_list = [[i]*4 for i in range(3)]
print(arr_list)