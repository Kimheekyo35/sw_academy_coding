# 엡실론을 포함한 연산에 주의하라
# 코테에서 부동소수형 데이터를 다룰 일이 생겼을 때 **엡실론 생각하기**

# 부동소수형 데이터를 활용하는 문제는 오차 허용 범위를 언급하는 경우가 많음.
def null():
    """
    파이썬은 부동소수형 데이터를 이진법으로 표현함.
    부동소수형 데이터 : 소수점이 고정되어 있지 않고 값의 크기에 따라 소수점 위치가 떠다니듯 바뀌는 방식으로 저장하기 때문 (3.14, 131.3545)
    파이썬에서 float 라고 불림.
    """
    return None

import sys

#엡실론 출력
print(sys.float_info.epsilon)

a = 0.1+0.1+0.1
b = 0.3
print(a-b) # 0이 아님

if abs(a-b) < sys.float_info.epsilon:
    print("a와 b 값은 같습니다")
    print(abs(a-b))
    print(sys.float_info.epsilon)
else:
    print("a와 b는 다른 값입니다.")