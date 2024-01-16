## 튜플 자료형 ##
# 리스트는 [], 튜플은 ()으로 둘러싼다.
# 리스트는 요솟값의 생성, 삭제, 수정이 가능하지만, 튜플은 요솟값을 바꿀 수 없다.
t1 = (1)
t2 = (1,) # 1개의 요소만을 가질 때 뒤에 쉼표를 붙여야 함
t3 = (1, 2, 3)
t4 = 1, 2, 3 # 소괄호 생략 가능
t5 = ('a', 'b', ('ab', 'cd'))
print(t3)

# 튜플 요소값을 삭제하거나 변경하려 할 때
# t1 = (1, 2, 'a', 'b')
# t1[0] = 'c'
'''Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment'''

# 인덱싱하기
t6 = (1, 2, 3, 4, 5)
print(t6[0])

# 슬라이싱하기
print(t6[3:])

# 튜플 더하기
t7 = (1, 2, 'a', 'b')
t8 = (3, 4)
t9 = t7 + t8
print(t9)

# 튜플 곱하기
t10 = t9 * 2
print(t10)

# 튜플 길이 구하기
print(len(t10))

# 튜플은 요솟값을 변경할수 없기 때문에 sort, insert, remove, pop과 같은 내장 함수가 없음


