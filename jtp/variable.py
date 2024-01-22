## 변수 ##
a = [1, 2, 3]
a2 = a
b = "python"
c = [1, 2, 3]
print(id(a)) # 4331214320 : 변수가 가리키고 있는 객체의 주소 값을 리턴
print(id(a2)) # a = a2

# 동일한 객체를 가리키고 있는지 판단하는 명령어 is
print(a is a2)
# a[0] = 4
print(a,a2) # a와 a2가 동일하게 바뀜

# 변수값을 가져오면서 다른 주소를 가르키도록 하는 법
# 1 : [:]
b2 = a[:]
a2[0] = 4
print(a, a2, b2)

# 2 : 카피 모듈 이용하기
from copy import copy
a3 = [1, 2, 3, 4]
b3 = copy(a3) # b = a3[:]
print(a3, b3)
print(a3 is b3)
# 리스트 자료형의 자체 함수인 copy 함수를 사용해도 copy 모듈을 사용하는 것과 결과가 동일함
a4 = [1, 2, 3]
b4 = a4.copy()
print(b4 is a4)
print(b4)
False

# 변수를 만드는 여러가지 방법
a5, b5 = ('python', 'life') # (a5, b5) = 'python', 'life'
# 튜플은 괄호 생략 가능

# 리스트로 변수 만들기
[a6, b6] = ['python', 'life']
print(a6)
# 여러 변수에 같은 값 대입
a7 = b7 = 'python'
print(a7 is b7) # True

# 값 바꾸기
[b6, a6] = ['life', 'python']
print(b6)